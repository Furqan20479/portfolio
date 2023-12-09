from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def base_view(request):
    if request.user.is_anonymous:

        return redirect('/login')
    
    return render(request, 'layout/base.html')
def login_view(request):
    if request.method =="POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
             return render(request, 'accounts/login.html')


    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)

    return redirect('/login')




               
