from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet  # Import de UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# Compare this snippet from users/views.py: