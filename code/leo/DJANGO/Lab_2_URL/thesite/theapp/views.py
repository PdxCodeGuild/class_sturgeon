import random

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect

from .models import Encoder

forcode = ['A','B','C','D','E','F','G','H','1','2','3','4','5']

def index(request):
    
    if request.method=='POST':
        code = list()
        for x in range(5):
            code.append(random.choice(forcode))
        code = ''.join(code)

        encoder = Encoder()
        encoder.url = request.POST['url']
        encoder.code = code
        encoder.save()

        context = {
            'code': code,
            'url': request.POST['url'],
        }
        return render(request, 'index.html', context)
   
    elif request.method=="GET":

        return render(request, 'index.html')

def redirec(request, shortcode):

    url_obj = get_object_or_404(Encoder, code=shortcode)
    aaa = url_obj.url
    bbb = str("Https://www." + aaa )

    return HttpResponseRedirect(bbb)

