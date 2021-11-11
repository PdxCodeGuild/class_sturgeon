from django.shortcuts import render
from django.http import HttpResponse
from .models import post



def index(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'chirp_app/index.html', context)

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')
