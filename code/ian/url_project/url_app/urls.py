from django.urls import path
from . import views

app_name='url_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('short/', views.short, name='short'),
    path('redirect/<str:short>/', views.url_redirect, name='redirect'),
]