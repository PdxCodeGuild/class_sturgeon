from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('mark_complete/<int:pk>', views.mark_complete, name='mark_complete'),
    path('<int:pk>/delete', views.delete, name='delete'),
]