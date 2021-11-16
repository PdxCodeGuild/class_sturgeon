from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

import random
import string

from .models import UrlDb


def index (request):
    if request.method == 'GET':
        context = {
            'url_list': UrlDb.objects.all(),
        }
        return render(request, 'url_shortener/index.html', context)
    elif request.method =='POST':
        url_db = UrlDb()
        url_db.long_url = request.POST['long-url']
        url_db.short_url = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
        url_db.save()
        context = {
            'url_list': UrlDb.objects.all(),
            'current_url': url_db,
        }
        return render(request, 'url_shortener/index.html', context)
        



def url_redirect (request, short_url):
    url_object = get_object_or_404(UrlDb, short_url=short_url)
    return HttpResponseRedirect(url_object.long_url)