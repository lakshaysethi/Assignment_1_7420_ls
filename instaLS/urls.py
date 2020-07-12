from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.start, name='start'),
    path('login/', views.loginUser, name='login'),
#path('forgot/', views.forgot, name='forgot'),
path('profile/', views.profile, name='profile'),
path('profile/edit/', views.editProfile, name='edit-profile'),
path('addpost/', views.addPost, name='addPost'),
path('explore/', views.explore, name='explore'),
path('home/', views.home, name='home'),
path('logout/', views.logoutUser, name='logout'),
path('search/', views.search, name='search'),
#path('addpost/', FaceCreateView.as_view(), name='addPost'),
path('like/', views.like, name='like'),


path('forgot/',
     auth_views.PasswordResetView.as_view(template_name="forgot.html"),
     name="forgot"),

path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name="password_reset_done"),

path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
     name="password_reset_confirm"),

path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
        name="password_reset_complete"),

]