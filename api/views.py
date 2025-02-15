from rest_framework import viewsets  # type: ignore
from softdesk.models import Project, Issue, Comment, Contributor
from softdesk.serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
from softdesk.pagination import CustomPagination
from softdesk.permissions import IsProjectAuthor, IsContributorOrReadOnly, IsAuthorOrReadOnly

class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les projets.
    Seul l'auteur d'un projet peut le modifier ou le supprimer.
    Les contributeurs peuvent uniquement voir le projet.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    permission_classes = [IsProjectAuthor | IsContributorOrReadOnly]


class IssueViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les issues.
    Seuls les contributeurs du projet lié peuvent voir et créer des issues.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    pagination_class = CustomPagination
    permission_classes = [IsContributorOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les commentaires des issues.
    Seul l'auteur du commentaire peut le modifier ou le supprimer.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthorOrReadOnly]


class ContributorViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les contributeurs.
    Seuls les auteurs des projets peuvent ajouter ou retirer des contributeurs.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    pagination_class = CustomPagination
    permission_classes = [IsProjectAuthor]
