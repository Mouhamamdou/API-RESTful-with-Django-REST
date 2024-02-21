from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Project, Issue, Comment


class IsAuthorOrContributor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Project):
            project = obj
        elif isinstance(obj, Issue):
            project = obj.project
        elif isinstance(obj, Comment):
            project = obj.issue.project
        else:
            return False

        is_author = obj.author == request.user

        is_contributor = project.contributors.filter(id=request.user.id).exists()

        if request.method in SAFE_METHODS:
            return is_author or is_contributor

        return is_author
