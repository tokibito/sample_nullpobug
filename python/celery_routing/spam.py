import os
from celery import Celery

app = Celery('spam', backend='amqp', broker='amqp://guest@localhost//')

@app.task
def hello():
    return os.getpid()

# hello.apply_async(queue='test')
