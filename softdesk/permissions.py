from rest_framework import permissions
from .models import Contributor, Project, Issue, Comment

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permission qui permet aux auteurs de modifier/supprimer leurs objets,
    mais donne seulement un accès en lecture aux autres utilisateurs.
    """

    def has_object_permission(self, request, view, obj):
        # Les permissions de lecture sont autorisées pour toutes les requêtes GET, HEAD ou OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Seul l'auteur peut modifier/supprimer
        return obj.author == request.user


class IsContributor(permissions.BasePermission):
    """
    Permission qui permet aux contributeurs d'un projet d'accéder aux ressources
    (projets, issues, commentaires). Les autres utilisateurs n'ont qu'un accès en lecture.
    """

    def has_object_permission(self, request, view, obj):
        project_id = view.kwargs.get('project_pk')
        if project_id :
            return Contributor.objects.filter(project_id=project_id, user=request.user).exists()     
        return False
