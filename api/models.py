from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Finished', 'Finished')])
    priority = models.CharField(max_length=50, choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')])
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
