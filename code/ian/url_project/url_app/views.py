
from django.http.request import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
import random
import string
from django.db import models

from url_app.models import UrlItem, Click


# Create your views here.
def index(request):

    return render(request, 'url_app/index.html')

def short(request):
    link = UrlItem(long=request.POST['link'])

    code = ''
    x = string.ascii_letters + string.digits
    while len(code) < 6:
        code += random.choice(x)
    link.short = code
    link.save()
    
    context = {'link': link, 'code': code}
    return render(request, 'url_app/index.html', context)


def url_redirect(request, short):
    m = request.META   
    
    link = get_object_or_404(UrlItem, short=short)
    link.clicks += int(1)    

    new_data = Click()
    new_data.urlitem = link
    new_data.username = m['USERNAME']
    new_data.computer_name = m['COMPUTERNAME']
    new_data.os = m['OS']
    
    new_data.save()   
    link.save()
    
    return redirect(f'{link.long}')  