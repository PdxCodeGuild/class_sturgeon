from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'posts'

urlpatterns = [
    path('', login_required(views.PostFeedView.as_view()), name='feed'),
    path('posts/new/', views.CreatePostView.as_view(), name='create_post'),
    path('posts/<int:post_id>/', login_required(views.PostDetailView.as_view()), name='detail'),
    path('posts/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('posts/<int:comment_id>/comments/delete', views.delete_own_comment, name='delete_own_comment'),
]