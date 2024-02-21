from django.db import models
from django.conf import settings
import uuid


class Project(models.Model):
    TYPE_CHOICES = (
        ('back-end', 'Back-end'),
        ('front-end', 'Front-end'),
        ('iOS', 'iOS'),
        ('Android', 'Android'),
    )

    title = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authored_projects')
    created_time = models.fields.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='contributed_projects')


class Issue(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )

    BALISE_CHOICES = (
        ('bug', 'Bug'),
        ('feature', 'Feature'),
        ('task', 'Task')
    )

    STATUS_CHOICES = (
        ('TO_DO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('FINISHED', 'Finished')
    )

    titre = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authored_issue')
    contributor = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='contributed_issue', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    balise = models.CharField(max_length=50, choices=BALISE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='TO_DO')
    created_time = models.fields.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authored_comment')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField()
    created_time = models.fields.DateTimeField(auto_now_add=True)

