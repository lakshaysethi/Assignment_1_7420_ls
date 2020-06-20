from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django import forms
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AddPostForm
# from tasks import app
# Create your views here.
from .models import Post, Profile, Like
from . import email_test
from time import sleep
import time as timer_wait
from .send_email import sendEmailWithSendGrid
from django.core.mail import send_mail
def start(request):
    print("starting add with delay")
    add.delay(2,3,str(request.META))
    title = 'Welcome!'
    context = {'title': title}
    if(request.user.is_authenticated):
        return redirect( 'home' )
    try:
        if (request.method == 'POST'):
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            user = User.objects.create_user(username, email, password)

            if user is not None:
                sendWelcomeEmail(user)
                msg = "your account was created successfully please log in now"
                # messages.add_message(request, level, message, extra_tags='', fail_silently=False)
                messages.add_message(request, messages.INFO, msg)
                #email_test.send_email(user.email,user.username,msg,'Welcome to instaLS')
                # A backend authenticated the credentials
                return redirect( 'login')
    except IntegrityError:
        messages.add_message(request, messages.INFO, "That Username is taken please try another username")

    return render(request, 'firstPage.html', context)


def loginUser(request):

    title = 'Login!'
    context = {'title': title}
    if (request.user.is_authenticated):
        return redirect( 'home'  )
    if(request.method =='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, "please check your username and/or password")

    return render(request, 'login.html', context)


def logoutUser(request):
    if (request.user.is_authenticated):
        logout(request)


    return redirect( 'login'  )



def home(request):
    if(not request.user.is_authenticated):
        return redirect('start')
    title = 'Wall'
    
    postsData = []
    for post in Post.objects.all():
        if post.likes.filter(user=request.user).first() is not None:
            unit = {'post':post,"likeByCurrentUser":post.likes.filter(user=request.user).first()}
        else:
            unit = {'post':post}
        postsData.append(unit)


    context = {'title': title,'postsData':postsData}
    return render(request, 'wall.html', context)



# def forgot(request):
#     if ( request.user.is_authenticated):
#         return redirect('home')
#     title = 'Forgot Password!'
#     context = {'title': title}
#     if(request.method =="POST"):
#         email = request.POST.get('email')
#         return redirect('reset_password')
#
#
#     return render(request, 'forgot.html', context)


def profile(request):
    if (not request.user.is_authenticated):
        return redirect('start')
    title = 'Profile'
    following = request.user.profile.following.all()
    postsData = []
    likes = request.user.like_set.all()
    for like in likes:
        unit = {'post':like.post_set.first(),'likeByCurrentUser':like}
        postsData.append(unit)

    myPosts = []
    allmyPosts = request.user.profile.post_set.all()
    for post in allmyPosts:
        unit = {'post':post,'likeByCurrentUser':post.likes.filter(user=request.user).first()}
        myPosts.append(unit)

    context = {'title': title,'myPosts':myPosts,'following':following,'postsData':postsData}


    return render(request, 'profile.html', context)


def like(request):   
    # email_test.print_email()
    #email_test.like_email() 
    if request.method == 'POST':
        #print("the post you liked is :"+ request.POST.get('postId'))
        #print("the emoji you clicked was :"+request.POST.get('emoji'))
        post = Post.objects.get(id=request.POST.get('postId'))
        if post.likes.all().filter(user=request.user).first() is not None:
            if str(post.likes.all().filter(user=request.user).first().emoji) == request.POST.get('emoji'):
                post.likes.all().filter(user=request.user).delete()
                return redirect('home')
            #delete old like
            post.likes.all().filter(user=request.user).delete()
        like = Like.objects.create(user=request.user, emoji=int(request.POST.get('emoji')))
        post.likes.add(like)
    
    return redirect('home')

@login_required
def addPost(request):
    if (not request.user.is_authenticated):
        return redirect('start')
    title = 'Add Post!'
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)
            post.by = request.user.profile
            post.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context = {'title': title, "form": form}

    return render(request, 'addpost.html', context)


def explore(request):
    if (not request.user.is_authenticated):
        return redirect('start')
    title = 'Explore!'
    context = {'title': title,'users':User.objects.all()}
    if(request.method=='POST'):
        profileId = request.POST.get('profileId')
        if(profileId is  not None):
            p1= Profile.objects.get(pk= profileId)
            request.user.profile.following.add(p1)
            messages.success(request, f'{p1.user.username} was added to your following list')




    return render(request, 'explore.html', context)

@login_required
def editProfile(request):
    if (not request.user.is_authenticated):
        return redirect('start')
    title = 'Edit Profile'
    context = {'title': title}

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated Successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context['u_form']= u_form
    context['p_form']= p_form


    return render(request, 'edit-profile.html', context)


def search(request):
    posts = []
    keyword = request.POST.get('searchText')
    for p1 in Post.objects.all():
        if str(p1.title).find(keyword) > -1 or str(p1.body).find(keyword) > -1 :
            posts.append(p1)



    context = {'posts':posts,'search':keyword}
    return render(request, 'search.html', context)




def sendWelcomeEmail(user):
    customMessage = {'to_emails':user.email,
                    'subject':'Welcome to Activity Management System',
                    'plain_text_content' : f'Welcome {user.username}',
                    'html_content': f'<h1>Welcome! {user.username}</h1><p>Thanks for joining</p>'}
    
    sendEmailWithSendGrid(customMessage)

# @app.task
# def add(x, y,request):
#     print(f'{request}')
#     print("please wait im adding maybe you want to count till 30?")
#     for i in range(0,5):
#         sleep(1)
#         print(i)
#         print(x+y)
#     send_mail(
#         'Notification from InstaClone celery',
#         f'{request}',
#         'lakshaynew@gmail.com',
#         ['lakshaynew@gmail.com'],
#         fail_silently=False,
#     )
#     return x + y