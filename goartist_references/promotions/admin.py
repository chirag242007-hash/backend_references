from django.contrib import admin

# Register your models here.

from .models import ArtistProfile, Artwork

admin.site.register(ArtistProfile)
admin.site.register(Artwork)