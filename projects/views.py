from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorSerializer
from softdesk.pagination import CustomPagination
from .permissions import IsProjectAuthor, IsContributorOrReadOnly



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsProjectAuthor]  # 🔥 Ajout des permissions

class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsContributorOrReadOnly]  # 🔥 Permissions
