from rest_framework import viewsets
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ProjectListSerializer, IssueListSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrContributor
from django.core.exceptions import PermissionDenied
from django.db.models import Q


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(Q(author=user) | Q(contributors=user))

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueSerializer

    permission_classes = [IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        user = self.request.user
        return Issue.objects.filter(Q(project__contributors=user) | Q(author=user))

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        return Comment.objects.filter(issue__project__contributors=self.request.user)

    def perform_create(self, serializer):
        issue = serializer.validated_data['issue']
        project = issue.project
        if not project.contributors.filter(id=self.request.user.id).exists():
            raise PermissionDenied("Vous devez être un contributeur du projet pour commenter cette issue.")
        serializer.save(author=self.request.user)

