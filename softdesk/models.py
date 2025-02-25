from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
import uuid

CustomUser = get_user_model()

class Project(models.Model):
    TYPE_CHOICES = [
        ('BACKEND', 'Back-end'),
        ('FRONTEND', 'Front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_projects")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    @property
    def project(self):
        return self

    def __str__(self):
        return self.name

class Contributor(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contributors")  # ✅ Corrigé la majuscule
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributions")

    class Meta:
        unique_together = ('user', 'project')  # ✅ Corrigé ici aussi

    def __str__(self):
        return f"{self.user.username} - {self.project.name}"

class Issue(models.Model):
    PRIORITY_CHOICES = [('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')]
    STATUS_CHOICES = [('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Finished', 'Finished')]
    TAG_CHOICES = [('BUG', 'BUG'), ('FEATURE', 'FEATURE'), ('TASK', 'TASK')]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="issues")
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_issues")
    assignee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="assigned_issues")  # ✅ Nom corrigé
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="softdesk_comments")  # ✅ Nom corrigé
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    @property
    def project(self):
        return self.issue.project

    def __str__(self):
        return f"comment by {self.author.username} on {self.issue.title}"
