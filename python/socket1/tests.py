import os
import time
import socket

def main():
    pid = os.fork()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if pid:
        time.sleep(2)
        s.connect(('localhost', 7777))
        s.send('A - %s' % pid)
    else:
        s.connect(('localhost', 7777))
        time.sleep(10)
        s.send('B - %s' % pid)
    s.close()

if __name__ == '__main__':
    main()
