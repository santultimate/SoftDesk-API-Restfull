from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProjectViewSet, IssueViewSet, CommentViewSet  # Correction ici

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# Compare this snippet from softdesk/views.py: