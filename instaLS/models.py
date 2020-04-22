
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Like(models.Model):
    user= models.ForeignKey(User,on_delete=models.PROTECT)
    emoji = models.IntegerField()

    def __str__(self):
        return f'by {self.user.username} emojiid: {self.emoji}'

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    following = models.ManyToManyField("self", symmetrical =False, blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'



class Post(models.Model):
    title= models.CharField(max_length=250)
    image = models.ImageField( null=True,blank=True,upload_to='posts')
    body = models.CharField(max_length=500)
    by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(Like,blank=True)

    def __str__(self):
        return f'{str(self.title)} post'

