from django.db.models.fields import DateTimeField 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db import models
from django.utils import timezone
from datetime import datetime

from grocery_app.models import GroceryItem


# Create your views here.
def index(request):
    c_item_list = GroceryItem.objects.filter(complete=True)
    inc_item_list = GroceryItem.objects.filter(complete=False)
    context = {'c_item_list': c_item_list, 'inc_item_list': inc_item_list}
    return render(request, 'grocery_app/index.html', context)

def create(request):
    new_item =GroceryItem(name=request.POST['new_item'])
    new_item.save()
    c_item_list = GroceryItem.objects.filter(complete=True)
    inc_item_list = GroceryItem.objects.filter(complete=False)
    context = {'c_item_list': c_item_list, 'inc_item_list': inc_item_list}

    return render(request, 'grocery_app/index.html', context)

def complete(request, pk):
    c_item_list = GroceryItem.objects.filter(complete=True)
    inc_item_list = GroceryItem.objects.filter(complete=False)
    context = {'c_item_list': c_item_list, 'inc_item_list': inc_item_list}
    comp_item = get_object_or_404(GroceryItem, pk=pk)
    if comp_item.complete == False:
        comp_item.complete = True
        comp_item.comp_date = datetime.now()
    elif comp_item.complete == True:
        comp_item.complete = False
    comp_item.save()
    return render(request, 'grocery_app/index.html', context)

def delete(request, pk):
    old_item = get_object_or_404(GroceryItem, pk=pk)
    c_item_list = GroceryItem.objects.filter(complete=True)
    inc_item_list = GroceryItem.objects.filter(complete=False)
    context = {'c_item_list': c_item_list, 'inc_item_list': inc_item_list}
    old_item.delete()
    return render(request, 'grocery_app/index.html', context)



