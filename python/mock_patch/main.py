import subprocess


def say(message):
    """echoコマンドでmessageを実行する
    """
    return subprocess.call(['echo', message])


def say_hello(somebody):
    """「Hello, {somebody}!」と画面に表示する関数
    """
    message = "Hello, {}!".format(somebody)
    return say(message)


if __name__ == '__main__':
    say_hello("tokibito")
