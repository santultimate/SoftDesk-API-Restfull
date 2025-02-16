from rest_framework import permissions

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


class IsContributorOrReadOnly(permissions.BasePermission):
    """
    Permission qui permet aux contributeurs d'un projet d'accéder aux ressources
    (projets, issues, commentaires). Les autres utilisateurs n'ont qu'un accès en lecture.
    """

    def has_object_permission(self, request, view, obj):
        # Lecture autorisée pour tout le monde
        if request.method in permissions.SAFE_METHODS:
            return True
        # Vérifie si l'utilisateur est contributeur du projet lié à l'objet
        return obj.project.contributors.filter(id=request.user.id).exists()


class IsProjectAuthor(permissions.BasePermission):
    """
    Permission qui permet uniquement à l’auteur d’un projet de le modifier ou supprimer.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
