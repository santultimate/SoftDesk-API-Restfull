from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle CustomUser.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'age', 'phone', 'password']
    
    def create(self, validated_data):
        """
        Crée un nouvel utilisateur.
        """
        user = CustomUser.objects.create_user(**validated_data)
        return user
            
        
        

