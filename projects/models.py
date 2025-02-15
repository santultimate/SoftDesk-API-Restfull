from django.conf import settings
from django.db import models

class Project(models.Model):
    TYPE_CHOICES = [
        ('BACKEND', 'Back-end'),
        ('FRONTEND', 'Front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_projects")
    created_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contributors")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributions")
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'user')  # Un même utilisateur ne peut pas être contributeur plusieurs fois du même projet

    def __str__(self):
        return f"{self.user.username} -> {self.project.name}"
