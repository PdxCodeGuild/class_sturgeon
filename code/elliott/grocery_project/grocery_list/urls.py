from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
     path('about/', views.about, name='about'),
     path('add-item/', views.add_item, name='add-item'),
     path('del/<int:pk>', views.del_item, name='del-item')
]
