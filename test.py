import requests
import getpass
from colorama import Fore, Style, init

init(autoreset=True)
BASE_URL = "http://localhost:8000/api/"
TEST_USER = [
    {"username": "testuser","password": "testuser","email": "yacouba.santara@yahoo.fr","age": 25,"phone": "+33612345678"},
    {"username": "alice", "password": "passAlice123*", "email": "alice@example.com", "age": 30, "phone": "+33611112222"},
    {"username": "bob", "password": "passBob123*", "email": "bob@example.com", "age": 28, "phone": "+33633334444"},
    {"username": "charlie", "password": "passCharlie123*", "email": "charlie@example.com", "age": 35, "phone": "+33655556666"}
]

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


def test_create_user(user_data):
    response = requests.post(BASE_URL + "users/", json=user_data)
    if response.status_code == 201:
        print(Fore.GREEN + f"Utilisateur {user_data['username']} créé avec succès.")
        return response.json().get("id")
    else:
        print(Fore.RED + f"Échec de la création de {user_data['username']}: {response.text}")
        return None

def test_request_token(user_data):
    response = requests.post(BASE_URL + "token/", json={"username": user_data["username"], "password": user_data["password"]})
    if response.status_code == 200:
        print(Fore.GREEN + f"Authentification réussie pour {user_data['username']}.")
        return response.json().get("access")
    else:
        print(Fore.RED + f"Échec de l'authentification de {user_data['username']}: {response.text}")
        return None

def test_list_users(token):
    response = requests.get(BASE_URL + "users/", headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        print(Fore.GREEN + "Liste des utilisateurs récupérée avec succès.")
        for result in response.json().get("results", []):  # 👀 Assure-toi que "results" est bien la clé correcte
            print(Fore.YELLOW + f"- {result['username']}")
    else:
        print(Fore.RED + "Échec de la récupération des utilisateurs.")


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
        #print_response(response,True)
        return True 
    else:
        #print_response(response,False)
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
    response = requests.post(BASE_URL + f"projects/{project_id}/issues/{issue_id}/comments/", json=TEST_COMMENT.copy(), headers={"Authorization": f"Bearer {token}"})
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
    data={
        "title":"New title",
        "description":"New description",
        "priority":"HIGH",
        "tag":"FEATURE",
        "status":"INPROGRESS",
        "assignee":1
        }
    
    response = requests.put(BASE_URL + f"projects/{project_id}/issues/{issue_id}/", json=data, headers
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
    data={
        "description":"New comment"
        }
    response = requests.put(BASE_URL + f"projects/{project_id}/issues/{issue_id}/comments/{comment_id}/", json=data, headers
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

    # 1️⃣ Saisie des informations utilisateur
    print(Fore.MAGENTA + "🟢 Test: Création d'un utilisateur...")
    
    user_data = {
        "username": input("Entrez un nom d'utilisateur: "),
        "password": getpass.getpass("Entrez un mot de passe: ")
    }

    user_id = test_create_user(user_data)
    if not user_id:
        return

    # 2️⃣ Récupération du token
    print(Fore.MAGENTA + "🟢 Test: Récupération du token...")
    token = test_request_token(user_data)
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


if __name__ == "__main__":
    main()
