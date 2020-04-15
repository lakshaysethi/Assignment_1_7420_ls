
# Create your models here.
from django.db import models


from django.contrib.auth.models import User
#
# class Person(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    



# class Profile(models.Model):
#     followers = models.CharField(max_length=200)
#     following = models.CharField(max_length=200)
    
    


# REF
# from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)