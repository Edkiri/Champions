"""Invitations permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from circles.models.invitations import Invitation

class IsSelfMember(BasePermission):
  """Allow access only to member owners."""

  def has_permission(self, request, view):
    """Let object permission grant access."""
    obj = view.get_object()
    return self.has_object_permission(request, view, obj)

  def has_object_permission(self, request, view, obj):
    """Let object permission grant access."""
    return request.user == obj.user