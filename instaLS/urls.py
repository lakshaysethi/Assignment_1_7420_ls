from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('login/', views.loginUser, name='login'),
path('forgot/', views.forgot, name='forgot'),
path('profile/', views.profile, name='profile'),
path('addpost/', views.addPost, name='addPost'),
path('explore/', views.explore, name='explore'),
path('home/', views.home, name='home'),
path('logout/', views.logoutUser, name='logout'),


]