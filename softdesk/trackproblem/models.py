from django.db import models
from django.conf import settings
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contributors')
    created_time = models.fields.DateTimeField(auto_now_add=True)


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


'''
@receiver(post_save, sender=Project)
def add_author_to_contributors(sender, instance, created, **kwargs):
    if created:
        instance.contributors.add(instance.author)
'''


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

