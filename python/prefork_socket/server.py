import os
import sys
import socket
import signal

child_processes = []

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
            sys.stdout.write('child process: pid=%d, getpid=%d\n' % (pid, os.getpid()))
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
            sys.stdout.write('pid=%d data=[%s]\n' % (os.getpid(), data))
            conn.send('pid=%d length=%d OK' % (os.getpid(), len(data)))
        conn.close()

def accept_sigterm(sig, status):
    for pid in child_processes:
        os.kill(pid, signal.SIGTERM)
    sys.exit(0)

if __name__ == '__main__':
    main('127.0.0.1', 5000, 3)
