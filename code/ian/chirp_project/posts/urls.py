from django.urls import path
from . import views
from posts.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('details/<int:pk>/', PostDetailView.as_view(), name="details"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('like/<int:pk>/', views.like, name='like')
   
]
