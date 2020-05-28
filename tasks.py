from time import sleep
import celery
from django.conf import settings
app = celery.Celery('instaLS')
import os
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

def add(x, y):
    sleep(30)
    return x + y

# git push heroku master
# heroku ps:scale worker=1
