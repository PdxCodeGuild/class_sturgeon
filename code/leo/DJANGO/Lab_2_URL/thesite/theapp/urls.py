from django.urls import path
from . import views


app_name = 'theapp'
urlpatterns = [
    path('', views.index, name = 'index'),
    path( '<str:shortcode>', views.redirec, name = 'redirec')
]