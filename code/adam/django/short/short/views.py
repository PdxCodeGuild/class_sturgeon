from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Short
from string import ascii_letters, digits
from django.conf import settings
from random import choice
from django.contrib import messages
import string
import random

# Main page
def index(request, error=False):
    return render(request, 'short/index.html', {'error': error})

# Recieve www.whaterver.com and convert it to a jumble of letters and numbers 6x long (change the range to make it more)
def createshorturl(request):
    ip_user = request.META['REMOTE_ADDR']
    if request.method == 'POST':
        new_url = ''.join(random.choice(string.ascii_letters)
            for x in range(6))
        user_url = request.POST["url"]
        secure_user_url = request.POST["secure_url"]
        if len(secure_user_url) > len(user_url):
            new_url = Short(user_url=secure_user_url, new_url=new_url, user_ip=ip_user)
        else:
            new_url = Short(user_url=user_url, new_url=new_url, user_ip=ip_user)
        new_url.save()

#The coolest ever little popup that lets you know your new url is ready
        messages.info(request,'Success! Next Step is to Follow the link below the submit button')
        return redirect('/')

def urlcreated(request):
    url=Short.objects.all()
    return render(request,'short/urls.html',{'url':url})

def url_link(request, for_the_function_in_views_from_urls):
    reference_me_to_find_user_url = Short.objects.get(new_url=for_the_function_in_views_from_urls)
    reference_me_to_find_user_url.times_used += 1
    reference_me_to_find_user_url.save()
    return HttpResponseRedirect(reference_me_to_find_user_url.user_url)

def delete_url(request, pk):
    Short.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/list')

