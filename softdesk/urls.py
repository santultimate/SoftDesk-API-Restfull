from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Bienvenue sur SoftDesk API",
        "endpoints": {
            "admin": "/admin/",
            "projects": "/api/projects/",
            "issues": "/api/issues/",
            "comments": "/api/comments/",
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', api_root),  # Ajout de la route pour "/"
]
