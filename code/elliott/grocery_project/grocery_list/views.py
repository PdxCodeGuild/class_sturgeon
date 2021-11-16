from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import user_list




def index(request):
     
     
     context = {
          'items': user_list.objects.all()
     }


     return render(request, 'grocery_list/index.html', context)

def about(request):
    return render(request, 'grocery_list/about.html')

def add_item(request):
     new_item = user_list()
     new_item.grocery = request.POST['Items']
     new_item.amount = request.POST['Amount']
     new_item.save()
     return HttpResponseRedirect(reverse('grocery_list:index'))

def del_item(request, pk):
     user_list.objects.filter(id=pk).delete()
     return HttpResponseRedirect(reverse('grocery_list:index'))