from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def start(request):
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


                # messages.add_message(request, level, message, extra_tags='', fail_silently=False)
                messages.add_message(request, messages.INFO, "your account was created successfully please log in now")

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
    context = {'title': title}
    return render(request, 'wall.html', context)



def forgot(request):
    if ( request.user.is_authenticated):
        return redirect('home')
    title = 'Forgot Password!'
    context = {'title': title}
    return render(request, 'forgot.html', context)


def profile(request):
    if (not request.user.is_authenticated):
        return redirect('start')
    title = 'Profile'
    context = {'title': title}
    return render(request, 'profile.html', context)


def addPost(request):
    if (not request.user.is_authenticated):
        return redirect('start')
    title = 'Add Post!'
    context = {'title': title}
    return render(request, 'addpost.html', context)


def explore(request):
    if (not request.user.is_authenticated):
        return redirect('start')
    title = 'Explore!'
    context = {'title': title}
    return render(request, 'explore.html', context)


def editProfile(request):
    if (not request.user.is_authenticated):
        return redirect('start')
    title = 'Edit Profile'
    context = {'title': title}
    return render(request, 'edit-profile.html', context)