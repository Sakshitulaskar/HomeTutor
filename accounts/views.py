from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

def register(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        role = request.POST['role']


        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists'
            )

            return redirect('register')


        user = User.objects.create_user(

            username=username,

            email=email,

            password=password

        )


        Profile.objects.create(

            user=user,

            role=role

        )


        messages.success(
            request,
            'Registration Successful'
        )

        return redirect('login')


    return render(
        request,
        'register.html'
    )





def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user:

            login(request, user)

            if user.is_superuser:

                return redirect('/admin/')

            return redirect('home')


    return render(request, 'login.html')



def user_logout(request):

    logout(request)

    return redirect('home')