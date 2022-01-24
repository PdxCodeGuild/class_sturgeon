from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem

# Create your views here.

def index(request):
    completed = GroceryItem.objects.filter(completed=True).order_by('-completed_date')
    incomplete = GroceryItem.objects.filter(completed=False).order_by('created_date')
    context = {
        "complete_items" : completed,
        "incomplete_items" : incomplete
    }
    return render(request, "grocery_list/index.html", context)

def new(request):
    description = request.POST("description")
    GroceryItem.objects.create(description=description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse("grocery:index"))


def complete(request):
    pass 

def delete(reqest, pk):
    item = get_object_or_404(GroceryItem)
    item = delete
    return HttpResponseRedirect(reverse("grocery:index"))