from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = router.urls


# from .views import PostList, PostDetail

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]
