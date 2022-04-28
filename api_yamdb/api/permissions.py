from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Пермишн для проверки на владельца поста."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsSuperUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsModerator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'moderator'


class IsModeratorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'moderator'
