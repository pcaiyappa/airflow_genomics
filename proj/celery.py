from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('proj',
             broker='pyamqp://guest@localhost//',
             backend='db+postgresql://postgres:blindmelon@localhost:5432/celery_backend',
             include=['proj.tasks'])

if __name__ == '__main__':
    app.start()
