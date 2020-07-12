# from time import sleep
# import celery
# from Assignment_1_7420_ls import settings
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Assignment_1_7420_ls.settings')
 
# app = celery.Celery('Assignment_1_7420_ls')
# app.config_from_object('django.conf:settings')

# app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
#                 CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

 
# # Load task modules from all registered Django app configs.
# # app.autodiscover_tasks()




# @app.task
# def add(x, y):
#     print("please wait im adding maybe you want to count till 30?")
#     for i in range(0,30):
#         sleep(1)
#         print(i)
#         print(x+y)
#     return x + y

# # git push heroku master
# # heroku ps:scale worker=1
