from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import ArtistProfile, Artwork
from .serializers import ArtistProfileSerializer, ArtworkSerializer

class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer

class ArtworkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

from rest_framework import viewsets, permissions  # <-- Import permissions
from .models import ArtistProfile, Artwork
from .serializers import ArtistProfileSerializer, ArtworkSerializer

class ArtistViewSet(viewsets.ModelViewSet): # Changed from ReadOnlyModelViewSet
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer
    # Anyone can read, but only logged-in users can edit
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArtworkViewSet(viewsets.ModelViewSet): # Changed from ReadOnlyModelViewSet
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    # Anyone can read, but only logged-in users can edit
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
# ... your other imports ...

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    # Anyone should be able to access the registration page
    permission_classes = [permissions.AllowAny]

# Add this import at the top
from .permissions import IsOwnerOrReadOnly

# Update your ViewSets to use the new custom permission
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer
    # Replaced IsAuthenticatedOrReadOnly with our custom rule
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]