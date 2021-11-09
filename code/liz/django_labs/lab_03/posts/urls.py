from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.ChirpListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('create/', views.ChirpCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.ChirpDeleteView.as_view(), name='delete'),
]