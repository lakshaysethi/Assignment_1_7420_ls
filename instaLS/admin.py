from django.contrib import admin
from .models import Profile
from .models import Post,Like
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
# Register your models here.
