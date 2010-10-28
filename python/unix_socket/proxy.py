import socket

SOCK_FILENAME = '/tmp/my_unix_socket'

def main():
    s_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_cli = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s_cli.connect(SOCK_FILENAME)

    s_srv.bind(('0.0.0.0', 8000))
    s_srv.listen(1)
    try:
        try:
            while True:
                conn, addr = s_srv.accept()
                print '---connected---'
                data = conn.recv(1024)
                print data
                print '-----client------'
                # proxy client
                s_cli.send(data)
                content = s_cli.recv(1024)
                print content
                print '-----proxy-------'
                conn.send(content)
                conn.close()
        finally:
            s_cli.close()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
