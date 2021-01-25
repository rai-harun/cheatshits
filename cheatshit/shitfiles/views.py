from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='userlogin')
def ShitHome(request):
    titles = CheatShitFor.objects.filter(user=request.user)
    context = {
        'titles': titles,
    }
    return render(request, 'shitfiles/index.html', context)

def ShitDetails(request, pk):
    for 
    context = {

    }
    return render(request, 'shitfiles/index.html', context)