"""Users URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('me/profile/', views.UpdateProfileView.as_view(), name='update_profile'),

    # Posts
    path('<str:username_slug>/', login_required(views.UserDetailView.as_view()), name='detail'),
]