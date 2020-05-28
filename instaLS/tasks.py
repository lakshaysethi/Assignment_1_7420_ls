from time import sleep
import celery
app = celery.Celery('example')
import os
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])


def add(x, y):
    sleep(30)
    return x + y

# git push heroku master
# heroku ps:scale worker=1
