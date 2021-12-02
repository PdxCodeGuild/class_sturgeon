
from django.urls import path
from .views import Detailpokemon, Listpokemon
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('pokemon', Listpokemon.as_view()),
    path('pokemon/<int:pk>/', Detailpokemon.as_view()),
    ]