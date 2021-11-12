from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

my_app = 'url_app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.add, name = 'create'),
    path('<str:pk>', views.shorten, name = 'shorten')
]