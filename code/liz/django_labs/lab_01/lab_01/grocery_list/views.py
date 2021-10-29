from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

# Create your views here.
def home (request):
    latest_grocery_list = GroceryItem.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    context = {'latest_grocery_list': latest_grocery_list}
    return render(request, 'grocery_list/index.html', context)
    

def create (request, pk):
    return HttpResponse('create item')

def mark_complete (request, pk):
    return HttpResponse('mark complete/incomplete')

def delete (request, pk):
    return HttpResponse('delete item')