from django.urls import path, include


from . import views

app_name = 'users'

urlpatterns = [
    path('newuser/', views.NewUser.as_view(), name='newuser'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
   

]