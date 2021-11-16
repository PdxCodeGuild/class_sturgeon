from django.urls import path
from . import views

app_name = "grocery_list"

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name='new' ),
    path('delete/<int:pk>/', views.delete, name="delete"),
]
