from rest_framework import serializers
from .models import ArtistProfile, Artwork

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['id', 'title', 'image', 'description', 'created_at']

class ArtistProfileSerializer(serializers.ModelSerializer):
    # Nests the artwork data inside the artist profile response
    artworks = ArtworkSerializer(many=True, read_only=True)

    class Meta:
        model = ArtistProfile
        fields = ['id', 'user', 'bio', 'location', 'website', 'artworks']


from django.contrib.auth.models import User
# ... your other imports ...

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # This function safely creates the user and hashes their password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user