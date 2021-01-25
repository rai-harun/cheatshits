from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have logged in successfully')
            return redirect('shithome')
        else:
            messages.error(request, 'Try with correct credentials')

        print(username)
    context = {
    }
    return render(request, 'account/login.html', context)

def UserView(request):

    return render(request, 'account/details.html')

def UserLogout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('userlogin')