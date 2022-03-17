from platformdirs import user_cache_dir

from rest_framework import permissions

class IsReviewer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.Reviewer == request.user