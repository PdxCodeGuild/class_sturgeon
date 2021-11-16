from django.urls import path
from . import views

app_name = 'groceries' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
]