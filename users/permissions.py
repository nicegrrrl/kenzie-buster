from rest_framework import permissions


class LoggedUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        if request.user.is_employee or request.user.username == user.username:
            return True
