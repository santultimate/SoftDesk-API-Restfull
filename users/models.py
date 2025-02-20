from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """Manager personnalisé pour le modèle CustomUser"""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Modèle personnalisé d'utilisateur"""
    
    username = None  # Supprime le champ username par défaut
    email = models.EmailField(unique=True)  # Utilise l'email comme identifiant unique
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name="customuser_groups",
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="customuser_permissions",
        blank=True
    )

    objects = CustomUserManager()  # Associe le manager personnalisé
    
    USERNAME_FIELD = 'email'  # Définit l'email comme identifiant principal
    REQUIRED_FIELDS = []  # Pas d'autres champs obligatoires

    def __str__(self):
        return self.email


class Comment(models.Model):
    """Modèle pour les commentaires"""
    
    author = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name="comments"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.email} on {self.created_at}"
