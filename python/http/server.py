import os
import socket

content = b'HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 12\r\n\r\nHello world!'

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(("127.0.0.1", 80))
    s.listen(1)
    try:
        while True:
            conn, addr = s.accept()
            print('---connected---')
            try:
                while True:
                    data = conn.recv(1024)
                    print(data)
                    print('-------------------------')
                    conn.send(content)
            except KeyboardInterrupt:
                raise
            except:
                pass
            finally:
                conn.close()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
