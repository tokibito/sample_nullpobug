import os
import sys
import socket
import signal

child_processes = []

content = 'HTTP/1.0 200 OK\nContent-Type: text/plain\n\nHello world\n'
content_length = len(content)

def main(host, port, children):
    signal.signal(signal.SIGTERM, accept_sigterm)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    # fork
    for i in range(children):
        pid = os.fork()
        if pid != 0:
            # parent
            #sys.stdout.write('child process: pid=%d, getpid=%d\n' % (pid, os.getpid()))
            child_processes.append(pid)
        else:
            # child
            break

    if pid != 0:
        # wait for child
        os.wait()
    else:
        # accept
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024)
            #sys.stdout.write('pid=%d data=[%s]\n' % (pid, data))
            conn.send(content, content_length)
        conn.close()

def accept_sigterm(sig, status):
    for pid in child_processes:
        os.kill(pid, signal.SIGTERM)
    sys.exit(0)

if __name__ == '__main__':
    main('0.0.0.0', 8000, 5)
