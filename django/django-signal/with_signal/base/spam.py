from .signals import spam_main

def main():
    print("base/spam")
    spam_main.send(main, param="by base")

