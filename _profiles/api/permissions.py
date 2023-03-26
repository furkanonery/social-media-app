from rest_framework import permissions

permissions.IsAuthenticatedOrReadOnly

class ownProfileOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user ==
            obj.user
            )
    
class ownProfileStatusOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user ==
            obj.user_profile.user
            )
