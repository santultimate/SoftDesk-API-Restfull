from django.conf import settings  # Import settings
from django.db import models
import uuid

class Project(models.Model):
    TYPE_CHOICES = [('BACKEND', 'Back-end'), ('FRONTEND', 'Front-end'), ('IOS', 'iOS'), ('ANDROID', 'Android')]
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 🔥 Correction ici
    created_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

class Issue(models.Model):
    PRIORITY_CHOICES = [('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')]
    STATUS_CHOICES = [('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Finished', 'Finished')]
    TAG_CHOICES = [('BUG', 'BUG'), ('FEATURE', 'FEATURE'), ('TASK', 'TASK')]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 🔥 Correction ici
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignee', null=True, blank=True)  # 🔥 Correction ici
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 🔥 Correction ici
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

class Contributor(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 🔥 Correction ici
    created_time = models.DateTimeField(auto_now_add=True)
