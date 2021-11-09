from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.profile, name='profile'),
]