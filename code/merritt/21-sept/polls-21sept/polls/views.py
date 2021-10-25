from django.http import HttpResponse

def index(request):
    # our shell stuff goes here
    return HttpResponse("Hello World")