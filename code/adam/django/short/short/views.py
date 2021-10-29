from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Short
from string import ascii_letters, digits
from django.conf import settings
from random import choice
from django.contrib import messages
import string
import random

# Main page
def index(request):
    return render(request, 'short/index.html')

# Recieve www.whaterver.com and convert it to a jumble of letters and numbers 6x long (change the range to make it more)
def createshorturl(request):
    if request.method == 'POST':
        new_url = ''.join(random.choice(string.ascii_letters)
            for x in range(6))
        user_url = request.POST["url"]
        new_url = Short(user_url=user_url, new_url=new_url)
        new_url.save()
#The coolest ever little popup that lets you know your new url is ready
        messages.info(request,'Success!! Go to the url list to see your new url')
        return redirect('/')

def urlcreated(request):
    url=Short.objects.all()
    return render(request,'short/urls.html',{'url':url})