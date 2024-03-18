

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Check if user with given username or email already exists
        if Users.objects.filter(username=username).exists() or Users.objects.filter(email=email).exists():
            messages.error(request, 'Username or Email is already taken')
            return redirect('register')
        else:
            # Create new user
            user = Users.objects.create(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    return render(request, 'register.html')


def dashboard(request):
    logged_in_user = request.session.get('logged_in_user')
    if logged_in_user:
        return render(request, 'dashboard.html', {'username': logged_in_user})
    else:
        return redirect('login')

def home(request):
    return render(request, 'home.html')

def Account_Manager(request):
    return render(request, 'Account Manager.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Check if user with given email and password exists
        user = Users.objects.filter(email=email, password=password).first()
        if user:
            request.session['logged_in_user'] = user.username  # Set username as logged-in user
            messages.success(request, 'Login successful')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    if 'logged_in_user' in request.session:
        del request.session['logged_in_user']
        messages.success(request, 'Logout successful')
    return redirect('home')

def Trade_Copier(request):
    return render(request, 'Trade Copier.html')

def Blog(request):
    return render(request, 'Blog.html')

def Pricing(request):
    return render(request, 'Pricing.html')

def Contact(request):
    return render(request, 'Contact.html')

def forget_password(request):
    return render(request, 'forget password.html')
