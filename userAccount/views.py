from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method =='POST':
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, 'Login success')
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        list(messages.get_messages(request)) ##Clear the messges while loading the page first time
        return render(request, 'login.html')

def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2 :
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "The Username is already exists")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "The email address is already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name, password=password1, email= email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
                print('user created')              
        else:
            messages.info(request, "The passwords not matching")
            return redirect('register')

    else:
        list(messages.get_messages(request)) ##Clear the messges while loading the page first time
        return render(request, 'register.html')