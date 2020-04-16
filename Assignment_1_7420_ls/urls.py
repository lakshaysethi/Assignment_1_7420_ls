from django.conf.urls.static import static
from django.contrib import admin

from django.urls import include, path

from Assignment_1_7420_ls import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('instaLS.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


