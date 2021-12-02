from django.urls import path
from .views import PokemonViewSet, UserViewSet, CurrentUserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('pokemon', PokemonViewSet, basename='pokemon')


urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view())
]
    

