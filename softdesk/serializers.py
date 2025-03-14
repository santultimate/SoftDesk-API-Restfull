from rest_framework import serializers # type: ignore
from .models import Project, Issue, Comment, Contributor

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['author', 'created_time']
        

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['id', 'project', 'author', 'created_time']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'issue', 'author', 'created_time']
        
class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
        read_only_fields = ['id', 'project']