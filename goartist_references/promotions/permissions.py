from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request (GET, HEAD or OPTIONS requests).
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed if the user matches the object's owner.
        # If it's an ArtistProfile, check obj.user. If it's an Artwork, check obj.artist.user
        if hasattr(obj, 'user'):
            return obj.user == request.user
        elif hasattr(obj, 'artist'):
            return obj.artist.user == request.user

        return False