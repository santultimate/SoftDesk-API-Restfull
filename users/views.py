from rest_framework import viewsets, serializers
from rest_framework.permissions import AllowAny 
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('username')
    serializer_class = UserSerializer  
    
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return super().get_permissions()
    
    def perform_create(self, serializer):
        age = serializer.validated_data.get('age',None)
        if age is not None and age < 18:
            raise serializers.ValidationError("L'âge doit être supérieur ou égal à 18 ans.")
        serializer.save()
        
        
        
    