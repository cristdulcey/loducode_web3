from rest_framework import serializers, status
from rest_framework.permissions import AllowAny

class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """

    def __init__(self, validate_owner=False):
        self.validate_owner = validate_owner

    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False

    def has_object_permission(self, request, view, obj):
        # check if user who launched request is object owner
        if self.validate_owner:
            return bool(obj.person == request.user)
        return True


class CustomAPIException(serializers.ValidationError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "error"

    def __init__(self, msg, code, status_code=None, fields=None):  #pylint: disable=W0231
        self.detail = {"error": {"status_code": code, "message": msg}}

        if fields is not None:
            self.detail["error"]["fields"] = fields

        if status_code is not None:
            self.status_code = status_code
