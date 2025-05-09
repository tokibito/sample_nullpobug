<?php
require_once(__DIR__ . '/signing.php');

define('APP_ROOT', dirname(__FILE__) . '/../../');
// DjangoのSECRET_KEY
define('APP_SECRET_KEY', 'django-insecure-cz_o02rl8*#(t$i*2xs^_j4s__$$0q928p5&_hk01zw5zd#$s9');
// セッションIDが記録されたCOOKIEのキー名
define('APP_SESSION_COOKIE_NAME', 'sessionid');
// セッションデータが格納されたDjangoのデータベース
define('APP_SESSION_DATABASE', 'sqlite:' . APP_ROOT . 'database/db.sqlite3');
// セッションデータのsalt
define('APP_SESSION_SALT', 'django.contrib.sessions.SessionStore');
// ログイン画面のURL
define('APP_LOGIN_URL', '/django/login/');

function redirectLoginPage() {
  // Djangoのログイン画面にリダイレクト
  header('Location: ' . APP_LOGIN_URL);
  exit;
}

// COOKIEからセッションIDを取得
$session_id = $_COOKIE[APP_SESSION_COOKIE_NAME] ?? null;
if ($session_id === null) {
  // セッションIDが存在しない場合、ログイン画面にリダイレクト
  redirectLoginPage();
}

// セッションIDが存在する場合、データベースからセッション情報を取得
$db = new PDO(APP_SESSION_DATABASE);
//$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$stmt = $db->prepare("SELECT session_key, session_data, expire_date FROM django_session WHERE session_key = :session_key");
$stmt->execute([':session_key' => $session_id]);
$row = $stmt->fetch(PDO::FETCH_ASSOC);
if ($row) {
  $session_data = $row['session_data'];
} else {
  // セッションIDが無効な場合、ログイン画面にリダイレクト
  redirectLoginPage();
}
// セッションの有効期限を確認
$expire_date = new DateTime($row['expire_date']);
if ($expire_date < new DateTime()) {
  // セッションが期限切れの場合、ログイン画面にリダイレクト
  redirectLoginPage();
}

// セッションデータをデコード
$session = django_signer_loads($session_data, APP_SECRET_KEY, APP_SESSION_SALT);

// ユーザー情報を取得
$user_id = $session['_auth_user_id'] ?? null;
if ($user_id === null) {
  // ユーザー情報が取得できない場合、ログイン画面にリダイレクト
  redirectLoginPage();
}

// ユーザー情報をデータベースから取得
$stmt = $db->prepare("SELECT id, username FROM auth_user WHERE id = :user_id");
$stmt->execute([':user_id' => $user_id]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);
if (!$user) {
  // ユーザー情報が無効な場合、ログイン画面にリダイレクト
  redirectLoginPage();
}

// セッションのカウンター値を更新
$session['counter'] = ($session['counter'] ?? 0) + 1;
// セッションデータをエンコード
$session_data = django_signer_dumps($session, APP_SECRET_KEY, APP_SESSION_SALT, true, true);
// セッションデータをデータベースに保存
$stmt = $db->prepare("UPDATE django_session SET session_data = :session_data WHERE session_key = :session_key");
$stmt->execute([':session_data' => $session_data, ':session_key' => $session_id]);
?>
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>PHP側の画面</title>
    <link crossorigin="anonymous" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" rel="stylesheet">
  </head>
  <body>
    <div class="container mt-5">
      <h1>PHP側の画面</h1>
      <p>ログイン中のユーザー: id=<?php echo $user['id'] ?> username=<?php echo $user['username'] ?></p>
      <p>これはPHPでレンダリングされた画面です。</p>
      <p>PHP側で更新したカウンター: <?php echo $session['counter'] ?></p>
      <p>Djangoのセッションデータ:</p>
      <pre><code><?php echo htmlspecialchars(print_r($session, true)); ?></code></pre>
      <div>
        <a href="/django/" class="btn btn-primary">Django側の画面へ</a>
      </div>
    </div>
  </body>
</html>