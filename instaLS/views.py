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

# Create your views here.
from .models import Post


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
    context = {'title': title,'posts':Post.objects.all()}
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
    context = {'title': title,'posts':request.user.profile.post_set.all()}


    return render(request, 'profile.html', context)


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
    context = {'title': title}
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







