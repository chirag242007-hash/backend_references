from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ArtistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=100) #local tagging
    website =models.URLField(blank=True)

    def __str__(self):
        return self.user.username

class Artwork(models.Model):
    artist = models.ForeignKey(ArtistProfile,related_name='artworks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artwork/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



