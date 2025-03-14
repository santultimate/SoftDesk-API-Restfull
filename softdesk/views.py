from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from .pagination import CustomPagination
from .permissions import IsAuthorOrReadOnly, IsContributor

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]  
    
    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project)  # Ajout automatique du créateur comme contributeur


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Contributor.objects.filter(project_id=project_id)
        return Contributor.objects.none()
        
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = get_object_or_404(Project, pk=project_id)
        if project.author != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à ajouter un contributeur à ce projet.")
        serializer.save(project=project)    
    

class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsContributor, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Issue.objects.filter(project_id=project_id)
        return Issue.objects.none()
    
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = get_object_or_404(Project, pk=project_id)
        
        # Correction : Vérifier si l'utilisateur est un contributeur
        if not project.contributors.filter(user=self.request.user).exists():
            raise PermissionDenied("Vous n'êtes pas autorisé à créer une issue pour ce projet.")
        
        serializer.save(project=project, author=self.request.user)
        

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributor]
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        issue_id = self.kwargs.get('issue_pk')
        if project_id and issue_id:
            return Comment.objects.filter(
                issue_id=issue_id,
                issue__project_id=project_id,
                issue__project__contributors__user=self.request.user
            ).order_by('created_time')
        return Comment.objects.none()

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = get_object_or_404(Project, pk=project_id)
        issue_id = self.kwargs.get('issue_pk')
        issue = get_object_or_404(Issue, pk=issue_id, project=project)

        # Correction : Vérification correcte des contributeurs
        if not project.contributors.filter(user=self.request.user).exists():
            raise PermissionDenied("Vous n'êtes pas autorisé à commenter cette issue.")
        
        serializer.save(issue=issue, author=self.request.user)
