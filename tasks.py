from time import sleep
import celery
from django.conf import settings
app = celery.Celery('instaLS')
import os
settings.configure()
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task
def add(x, y):
    print("please wait im adding maybe you want to count till 30?")
    for i in range(0,30):
        sleep(1)
        print(i)
        print(x+y)
    return x + y

# git push heroku master
# heroku ps:scale worker=1
