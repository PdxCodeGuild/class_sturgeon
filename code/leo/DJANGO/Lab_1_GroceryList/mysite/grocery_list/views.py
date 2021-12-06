from django.utils import timezone
from django.http.response import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import GroceryItems


def index(request):
    
    grocery_list = GroceryItems.objects.all()
    
    context = {
        'grocery_list': grocery_list,
    }

    return render(request, 'index.html', context)

def add(request):

    New_Item = request.POST['NewItem']
    
    GroceryItems.objects.create(Item_Name=New_Item, Date_Added=timezone.now(), Purchased=False)
    
    return HttpResponseRedirect(reverse('grocery_list:index'))

def purchased(request, id):
    
    Item = get_object_or_404(GroceryItems, pk=id)
    
    Date_Purchased = timezone.now()
    Item.Purchased = True
    Item.Date_Purchased = Date_Purchased
    Item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete(request, id):

    Item = get_object_or_404(GroceryItems, pk=id) 
    
    # Item = GroceryItems.objects.get(id=id)
    
    Item.delete()
   
    return HttpResponseRedirect(reverse('grocery_list:index'))