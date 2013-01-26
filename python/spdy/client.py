import socket
import ssl
import pprint

import bitstring

print('HAS_NPN={}'.format(ssl.HAS_NPN))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# wrap_socketだとnpn_protocolsオプションがサポートされてない
ssl_sock = ssl.SSLSocket(
    sock=s,
    ca_certs="/etc/ssl/certs/ca-certificates.crt",
    cert_reqs=ssl.CERT_REQUIRED,
    ssl_version=ssl.PROTOCOL_TLSv1,
    do_handshake_on_connect=True,
    suppress_ragged_eofs=True,
    npn_protocols=['http/1.1', 'spdy/3'],
)
ssl_sock.connect(('hoge.appspot.com', 443))

pprint.pprint(ssl_sock.selected_npn_protocol())
pprint.pprint(ssl_sock.getpeercert())

# TODO: SYN_STREAMを送ってレスポンスを得る
#ssl_sock.write()
frame = bitstring.BitStream(ssl_sock.read())
bits = frame.bin
width = 32
while bits:
    pprint.pprint(bits[:width])
    bits = bits[width:]

ssl_sock.close()
