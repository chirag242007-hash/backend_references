from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, ArtworkViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'artworks', ArtworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, ArtworkViewSet, RegisterView # <-- Import the new view

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'artworks', ArtworkViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), # <-- Add this line
    path('', include(router.urls)),
]