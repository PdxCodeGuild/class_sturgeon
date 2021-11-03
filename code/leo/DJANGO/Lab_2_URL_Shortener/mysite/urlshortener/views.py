from django.http import HttpResponse


def index(request):
    return HttpResponse("URLs App - Working in progress")
