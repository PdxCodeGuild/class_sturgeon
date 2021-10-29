from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/create/', views.create, name='create'),
    path('<int:pk>/mark_complete/', views.mark_complete, name='mark_complete'),
    path('<int:pk>/delete', views.delete, name='delete'),
]