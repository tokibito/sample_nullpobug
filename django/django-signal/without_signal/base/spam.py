from app1.egg import receiver as app1_receiver
from app2.egg import receiver as app2_receiver

def main():
    print("base/spam")
    app1_receiver("by base")
    app2_receiver("by base")
