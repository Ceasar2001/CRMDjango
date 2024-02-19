from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    #check to see if logging in
    if request.method == 'POST':
        first_name = request.POST['first_name']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, first_name=first_name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            messages.success(request, "Error while login attempt please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    pass