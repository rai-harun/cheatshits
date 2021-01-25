from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='userlogin')
def ShitHome(request):
    titles = CheatShitFor.objects.filter(user=request.user)
    cheatshits = CheatShitFor.objects.all().prefetch_related('cheatshitss')
    # print(cheatshits)
    # print(titles)
    context = {
        'titles': titles,
        'cheatshits': cheatshits
    }
    return render(request, 'shitfiles/index.html', context)

@login_required(login_url='userlogin')
def CheatShitForView(request):
    titles = CheatShitFor.objects.all()
    print(titles)
    context = {
        'titles': titles
    }
    return render(request, 'shitfiles/sidebar.html', context)