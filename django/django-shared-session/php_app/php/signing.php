<?php

function b62_encode(int $num): string
{
  if (!is_int($num) || $num < 0) {
    throw new InvalidArgumentException("Only non-negative integers allowed");
  }

  $chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
  $base = 62;

  if ($num === 0) {
    return '0';
  }

  $result = '';
  while ($num > 0) {
    $result = $chars[$num % $base] . $result;
    $num = intdiv($num, $base);
  }

  return $result;
}

function b62_decode(string $str): int
{
  $chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
  $base = 62;

  $num = 0;
  $len = strlen($str);
  for ($i = 0; $i < $len; $i++) {
    $pos = strpos($chars, $str[$i]);
    if ($pos === false) {
      throw new InvalidArgumentException("Invalid character in input: " . $str[$i]);
    }
    $num = $num * $base + $pos;
  }

  return $num;
}

function b64_encode($data): string
{
  if (!is_string($data)) {
    throw new InvalidArgumentException("Only strings allowed");
  }

  return rtrim(strtr(base64_encode($data), '+/', '-_'), '=');
}

function b64_decode($input)
{
  $remainder = strlen($input) % 4;
  if ($remainder) {
    $padlen = 4 - $remainder;
    $input .= str_repeat('=', $padlen);
  }
  return base64_decode(strtr($input, '-_', '+/'));
}

function salted_hmac($key_salt, $value, $secret_key, $algorithm = 'sha1')
{
  if (!is_string($value)) {
    $value = strval($value);
  }
  $key = hash($algorithm, $key_salt . $secret_key, true);
  $hmac = hash_hmac($algorithm, $value, $key, true);
  return $hmac;
}

class Signer
{
  protected string $sep;
  protected string $salt;
  protected string $secret;
  protected string $algorithm;

  public function __construct(string $secret, string $salt = 'django.core.signing.Signer', string $sep = ':', string $algorithm = 'sha256')
  {
    if (preg_match('/[' . preg_quote($sep, '/') . ']/', $salt)) {
      throw new InvalidArgumentException("Salt cannot contain the separator character");
    }
    $this->secret = $secret;
    $this->salt = $salt;
    $this->sep = $sep;
    $this->algorithm = $algorithm;
  }

  protected function get_signature(string $value): string
  {
    return b64_encode(salted_hmac($this->salt . 'signer', $value, $this->secret, $this->algorithm));
  }

  public function sign(string $value): string
  {
    return $value . $this->sep . $this->get_signature($value);
  }

  public function unsign(string $signed_value): string
  {
    $sep_pos = strrpos($signed_value, $this->sep);
    if ($sep_pos === false) {
      throw new RuntimeException("Bad signature");
    }

    $value = substr($signed_value, 0, $sep_pos);
    $sig = substr($signed_value, $sep_pos + strlen($this->sep));

    $expected_sig = $this->get_signature($value);

    if (!hash_equals($expected_sig, $sig)) {
      throw new RuntimeException("Signature does not match");
    }

    return $value;
  }
}

class TimestampSigner extends Signer
{
  protected string $timestamp_salt = 'django.core.signing.TimestampSigner';

  public function make_timestamp(): string
  {
    return b62_encode(time());
  }

  public function sign(string $value): string
  {
    $timestamp = $this->make_timestamp();
    $value_with_ts = $value . $this->sep . $timestamp;
    return parent::sign($value_with_ts);
  }

  public function unsign(string $signed_value, int|null $max_age = null): string
  {
    $result = parent::unsign($signed_value);
    $parts = explode($this->sep, $result);
    if (count($parts) !== 2) {
      throw new RuntimeException("Bad signature format");
    }

    [$value, $ts_b62] = $parts;

    if ($max_age !== null) {
      $timestamp = b62_decode($ts_b62);
      $age = time() - $timestamp;
      if ($age > $max_age) {
        throw new RuntimeException("Signature has expired");
      }
    }

    return $value;
  }

  public function timestamp(string $signed_value): int
  {
    $parts = explode($this->sep, $signed_value);
    if (count($parts) !== 3) {
      throw new RuntimeException("Bad signature format");
    }
    return b62_decode($parts[1]);
  }
}

function django_signer_dumps($value, string $secret, string $salt, bool $compress = false, bool $add_timestamp = false): string
{
  $json = json_encode($value, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);

  if ($compress) {
    $data = zlib_encode($json, ZLIB_ENCODING_DEFLATE);
  } else {
    $data = $json;
  }

  $b64 = b64_encode($data);
  // add a dot to the beginning of the string if compress is true
  if ($compress) {
    $b64 = '.' . $b64;
  }

  if ($add_timestamp) {
    $signer = new TimestampSigner($secret, $salt);
  } else {
    $signer = new Signer($secret, $salt);
  }

  return $signer->sign($b64);
}

function django_signer_loads(string $signed_value, string $secret, string $salt, int|null $max_age = null)
{
  // Use appropriate signer
  if (substr_count($signed_value, ':') === 2) {
    $signer = new TimestampSigner($secret, $salt);
    $b64 = $signer->unsign($signed_value, $max_age);
  } else {
    $signer = new Signer($secret, $salt);
    $b64 = $signer->unsign($signed_value);
  }

  // first character is a dot, indicating compression
  $is_compressed = false;
  if (strlen($b64) > 0 && $b64[0] === '.') {
    $is_compressed = true;
    $b64 = substr($b64, 1);
  }

  $raw = b64_decode($b64);
  if ($is_compressed) {
    $json = zlib_decode($raw);
  } else {
    $json = $raw;
  }

  if ($json === false) {
    throw new RuntimeException("Base64 decoding failed");
  }

  $data = json_decode($json, true);

  if (json_last_error() !== JSON_ERROR_NONE) {
    throw new RuntimeException("JSON decoding failed: " . json_last_error_msg());
  }

  return $data;
}
