from rest_framework import permissions

class isStafforReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return True if request.method in permissions.SAFE_METHODS else False