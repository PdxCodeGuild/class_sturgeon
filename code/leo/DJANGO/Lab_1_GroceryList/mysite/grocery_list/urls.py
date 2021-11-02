from django.urls import path
from . import views


app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name = 'add'),
    path('purchased/<int:id>', views.purchased, name='purchased'),
    path('remove/<int:id>', views.delete, name = 'delete'),
]