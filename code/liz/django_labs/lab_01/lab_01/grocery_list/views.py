from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

# Create your views here.
def home (request):
    latest_grocery_list = GroceryItem.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    completed_items = [item for item in GroceryItem.objects.all() if item.is_completed == True]
    incomplete_items = latest_grocery_list.filter(is_completed = False)
    context = {
        'latest_grocery_list': latest_grocery_list,
        'completed_items': completed_items,
        'incomplete_items': incomplete_items
        }
    return render(request, 'grocery_list/index.html', context)
    

def create (request):
    grocery_item = GroceryItem()
    grocery_item.item_text = request.POST['item-info']
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:home'))

def mark_complete (request, pk):
    grocery_item = get_object_or_404(GroceryItem, pk=pk)
    if grocery_item.is_completed == True:
        grocery_item.is_completed = False
    else:
        grocery_item.is_completed = True
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:home'))

def delete (request, pk):
    grocery_item = get_object_or_404(GroceryItem, pk=pk)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:home'))