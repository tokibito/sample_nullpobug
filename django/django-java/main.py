# coding: utf-8
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JAVA_CMD = 'java'
JAVA_CLASS_PATH = 'java_app/echo.jar'
JAVA_CLASS = 'echo'


def echo(message):
    command = [
        JAVA_CMD,
        '-cp',
        os.path.join(BASE_DIR, JAVA_CLASS_PATH),
        JAVA_CLASS,
        message.encode('utf-8')]
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    proc.wait()
    return proc.stdout.read().decode('utf-8')


if __name__ == '__main__':
    print(echo(u'日本語'))
