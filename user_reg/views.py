from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect("login")
        else:
            messages.info(request,"Password not same")
            return redirect('register')
    
    return render(request, "user_register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Username/Password is wrong")
    
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return render(request, "logout.html")
# Create your views here.
