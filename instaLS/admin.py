from django.contrib import admin
from .models import Profile
from .models import Post,Like
admin.site.register(Profile)
# admin.site.register(Post)
admin.site.register(Like)
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','body','image','date_posted','by__user__username']
    list_display = ['id','title','body','image','date_posted','by']
    fields = ['image','title','body','by','date_posted']
    readonly_fields = ['date_posted','by']
    list_editable = ['image','body','title']
    list_display_links = ['id',]
    list_filter = ['date_posted', ]
    
admin.site.register(Post,PostAdmin)