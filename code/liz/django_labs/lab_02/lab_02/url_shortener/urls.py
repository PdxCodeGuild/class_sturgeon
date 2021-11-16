from django.urls import path
from . import views

app_name = 'url_shortener' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/<str:short_url>', views.url_redirect, name='redirect'),
]