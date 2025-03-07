import requests
from colorama import Fore, Style, init

init(autoreset=True)
BASE_URL = "http://localhost:8000/api/"
TEST_USER = {
    "username": "testuser",
    "password": "test123*",
    "email": "yacouba.santara@yahoo.fr",
    "age": 25,
    "phone": "+33612345678"
}

TEST_PROJECT = {
    "name": "Test project",
    "description": "This is a test project",
    "type": "BACKEND"
}

TEST_ISSUE = {
    "title": "Test issue",
    "description": "This is a test issue",
    "priority": "LOW",
    "tag": "BUG",
    "status": "TODO",
    "assignee": None 
}

TEST_COMMENT = { 
    "description": "This is a test comment"
}   

def print_response(response,result):
    if result:
        print(Fore.GREEN + "Request successful.")
    else:
        print(Fore.RED + "Request failed.")      
        print(Fore.YELLOW + f"Status code: {response.status_code}")
        print(Fore.CYAN + f"Response:{response.text}")


def test_create_user():
    response = requests.post(BASE_URL + "users/", json=TEST_USER)
    if response.status_code == 201:
        print_response(response,True)
        return response.json().get("id")
    else:
        print_response(response,False)
        return None

def test_request_token():
    response = requests.post(BASE_URL + "token/", json={"username": TEST_USER["username"], "password": TEST_USER["password"]})
    if response.status_code == 200:
        print_response(response,True)
        return response.json().get("access")
    else:
        print_response(response,False)
        return None
    
def test_list_users(token):
    response = requests.get(BASE_URL + "users/", headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        print_response(response,True)
    else:
        print_response(response,False)
        return None

def test_create_project(token):
    response = requests.post(BASE_URL + "projects/", json=TEST_PROJECT, headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 201:
        print_response(response,True)
        return response.json().get("id")
    else:
        print_response(response,False)
        return None

def test_get_existing_project_id(token):
    response = requests.get(BASE_URL + f"projects/", headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        print_response(response,True)
        projects= response.json()
        if projects:
            return projects[0].get("id")
        else:
            return None
    else:
        print_response(response,False)
        return None

def test_add_contributor(token,project_id,user_id):
    response = requests.post(BASE_URL + f"projects/{project_id}/contributors/", json={"user":user_id,"role":"CONTRIBUTOR"}, headers
    ={"Authorization": f"Bearer {token}"})
    if response.status_code == 201:
        print_response(response,True)
        return True 
    else:
        print_response(response,False)
        return False
    
def test_create_issue(token,project_id):
    issue=TEST_ISSUE.copy()
    issue["assignee"]=1
    response = requests.post(BASE_URL + f"projects/{project_id}/issues/", json=issue, headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 201:
        print_response(response,True)
        return response.json().get("id")
    else:
        print_response(response,False)
        return None

def test_list_issues_for_project(token,project_id):
    response = requests.get(BASE_URL + f"projects/{project_id}/issues/", headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        print_response(response,True)
    else:
        print_response(response,False)

def test_create_comment(token,project_id,issue_id):
    response = requests.post(BASE_URL + f"projects/{project_id}/issues/{issue_id}/comments/", json=TEST_COMMENT, headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 201:
        print_response(response,True)
        return response.json().get("id")
    else:
        print_response(response,False)
        return None
    
def test_list_comments_for_issue(token,project_id,issue_id):
    response = requests.get(BASE_URL + f"projects/{project_id}/issues/{issue_id}/comments/", headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        print_response(response,True)
    else:
        print_response(response,False)
        
def test_edit_issue(token,project_id,issue_id):
    issue=TEST_ISSUE.copy()
    issue["title"]="New title"
    response = requests.put(BASE_URL + f"projects/{project_id}/issues/{issue_id}/", json=issue, headers
    ={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        print_response(response,True)
        return True
    else:
        print_response(response,False)
        return False
    
def test_delete_issue(token,project_id,issue_id):
    response = requests.delete(BASE_URL + f"projects/{project_id}/issues/{issue_id}/", headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 204:
        print_response(response,True)
        return True
    else:
        print_response(response,False)
        return False    
    
def test_edit_comment(token,project_id,issue_id,comment_id):
    comment=TEST_COMMENT.copy()
    comment["description"]="New description"
    response = requests.put(BASE_URL + f"projects/{project_id}/issues/{issue_id}/comments/{comment_id}/", json=comment, headers
    ={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        print_response(response,True)
        return True
    else:
        print_response(response,False)
        return False

def test_delete_comment(token, project_id, issue_id, comment_id):
    response = requests.delete(
        BASE_URL + f"projects/{project_id}/issues/{issue_id}/comments/{comment_id}/",
        headers={"Authorization": f"Bearer {token}"}
    )
    if response.status_code == 204:
        print_response(response, True)
        return True
    else:
        print_response(response, False)
        return False



def main():
    print(Fore.BLUE + "\n=== Début des tests ===\n")

    # 1️⃣ Créer un utilisateur
    print(Fore.MAGENTA + "🟢 Test: Création d'un utilisateur...")
    user_id = test_create_user()
    if not user_id:
        return

    # 2️⃣ Récupérer le token d'authentification
    print(Fore.MAGENTA + "🟢 Test: Récupération du token...")
    token = test_request_token()
    if not token:
        return

    # 3️⃣ Lister les utilisateurs (nécessite un token valide)
    print(Fore.MAGENTA + "🟢 Test: Liste des utilisateurs...")
    test_list_users(token)

    # 4️⃣ Créer un projet
    print(Fore.MAGENTA + "🟢 Test: Création d'un projet...")
    project_id = test_create_project(token)
    if not project_id:
        return

    # 5️⃣ Ajouter un contributeur au projet
    print(Fore.MAGENTA + "🟢 Test: Ajout d'un contributeur...")
    test_add_contributor(token, project_id, user_id)

    # 6️⃣ Créer une issue pour le projet
    print(Fore.MAGENTA + "🟢 Test: Création d'une issue...")
    issue_id = test_create_issue(token, project_id)
    if not issue_id:
        return

    # 7️⃣ Lister les issues du projet
    print(Fore.MAGENTA + "🟢 Test: Liste des issues...")
    test_list_issues_for_project(token, project_id)

    # 8️⃣ Ajouter un commentaire à l'issue
    print(Fore.MAGENTA + "🟢 Test: Création d'un commentaire...")
    comment_id = test_create_comment(token, project_id, issue_id)
    if not comment_id:
        return

    # 9️⃣ Lister les commentaires d'une issue
    print(Fore.MAGENTA + "🟢 Test: Liste des commentaires...")
    test_list_comments_for_issue(token, project_id, issue_id)

    # 🔟 Modifier une issue
    print(Fore.MAGENTA + "🟢 Test: Modification d'une issue...")
    test_edit_issue(token, project_id, issue_id)

    # 1️⃣1️⃣ Modifier un commentaire
    print(Fore.MAGENTA + "🟢 Test: Modification d'un commentaire...")
    test_edit_comment(token, project_id, issue_id, comment_id)

    # 1️⃣2️⃣ Supprimer un commentaire
    print(Fore.MAGENTA + "🟢 Test: Suppression d'un commentaire...")
    test_delete_comment(token, project_id, issue_id, comment_id)

    # 1️⃣3️⃣ Supprimer une issue
    print(Fore.MAGENTA + "🟢 Test: Suppression d'une issue...")
    test_delete_issue(token, project_id, issue_id)

    print(Fore.BLUE + "\n=== Fin des tests ===\n")


if __name__ == "__main__":
    main()
# Compare this snippet from softdesk/permissions.py:
# from rest_framework import permissions
#
# class IsAuthorOrReadOnly(permissions.BasePermission):