# SoftDesk API RESTful

## ✨ Présentation
SoftDesk est une API RESTful permettant la gestion de projets et le suivi des issues (problèmes, tâches, améliorations) avec un système de commentaires pour faciliter la communication entre les contributeurs.

## 📅 Fonctionnalités
- Gestion des utilisateurs (inscription, connexion avec JWT, vérification de l'âge selon RGPD)
- Gestion des projets et de leurs contributeurs
- Gestion des issues avec priorité, statut et balise
- Gestion des commentaires
- Authentification par JSON Web Token (JWT)
- Pagination des ressources

## ⚡ Prérequis
- Python 3.8+
- Pipenv ou Poetry (recommandé pour la gestion des dépendances)
- PostgreSQL (optionnel, SQLite utilisé par défaut)
- Git

## 🌟 Installation

### 1. Cloner le dépôt
```sh
git clone https://github.com/santultimate/SoftDesk-API-Restfull.git
cd SoftDesk-API-Restfull
```

### 2. Initialiser un dépôt Git
```sh
git init
git remote add origin https://github.com/santultimate/SoftDesk-API-Restfull.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 3. Créer un environnement virtuel et installer les dépendances
Avec **pipenv** :
```sh
pip install pipenv
pipenv install --dev
pipenv shell
```

Ou avec **Poetry** :
```sh
pip install poetry
poetry install
poetry shell
```

### 4. Configurer la base de données
Par défaut, SQLite est utilisé. Pour PostgreSQL, modifiez `settings.py` et renseignez vos informations.

Appliquer les migrations :
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Créer un superutilisateur (admin)
```sh
python manage.py createsuperuser
```

### 6. Lancer le serveur
```sh
python manage.py runserver
```
L'API est accessible sur **http://127.0.0.1:8000/api/**.

## 🛠️ Utilisation

- **Endpoints principaux** :
  - `POST /api/token/` : Obtenir un token JWT
  - `POST /api/token/refresh/` : Rafraîchir un token JWT
  - `GET /api/projects/` : Liste des projets
  - `POST /api/projects/` : Création d'un projet
  - `GET /api/issues/` : Liste des issues
  - `POST /api/issues/` : Création d'une issue
  - `GET /api/comments/` : Liste des commentaires
  - `POST /api/comments/` : Ajouter un commentaire

## 🔧 Tests
Utilisez **Postman**, `curl` ou l'interface web de Django REST Framework.

Exemple de requête avec `curl` :
```sh
curl -X GET http://127.0.0.1:8000/api/projects/ -H "Authorization: Bearer VOTRE_TOKEN"
```

## 🌐 Documentation
La documentation API sera disponible sous `http://127.0.0.1:8000/api/docs/` (si ajout de Swagger ou Redoc).

## 🔄 Contribution
Les contributions sont les bienvenues ! Forkez le projet et proposez vos PR.

## 🐝 Auteur
**Santultimate** - [GitHub](https://github.com/santultimate)

## 🛡️ Licence
Ce projet est sous licence MIT.

