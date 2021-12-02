from django.urls import path
from django.urls.resolvers import URLPattern
from .views import studentAPIView

urlpatterns = [
    path('', studentAPIView.as_view())
    ]