from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items

# Create your views here.

def shopping_list_view(request, error=False):
    item_list = Items.objects.order_by('id')
    context = {'item_list' : item_list}
    return render(request, 'shopping_list/shopping_list.html', {'error': error, 'items': Items.objects.order_by('content')})

def add_item_view(request):
    if request.POST['content']=='':
        return HttpResponseRedirect('/shopping_list/error')
    Items(content = request.POST['content']).save()
    return HttpResponseRedirect('/shopping_list/')

def delete_item_view(request, item_id):
    Items.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/shopping_list/')

#with this one, if we click it, the line goes through the middle and it's completed
def completeItem(request, item_id):
    item = Items.objects.get(pk=item_id)
    item.complete = True
    item.save()
    return redirect('/shopping_list/')

def uncompleteItem(request, item_id):
    item = Items.objects.get(pk=item_id)
    item.complete = False
    item.save()
    return redirect('/shopping_list/')