from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Assurez-vous que l'utilisateur est authentifié

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)  # Assure que `PUT` fonctionne

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Utilisateur supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
