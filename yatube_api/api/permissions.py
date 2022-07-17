from rest_framework import permissions


class NotAuthorPermission(permissions.BasePermission):
    """Object-level permission to only allow an author to edit it."""
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class FollowingPermission(permissions.BasePermission):
    """
    Object-level permission to only allow only requested user to be a follower.
    """
    message = 'Подписаться может только авторизованный пользователь!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
