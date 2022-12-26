from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('moderator:index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('moderator:index')

    return render(request, 'registration/login.html')

def signout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('submission:index')