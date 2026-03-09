import requests
from dotenv import load_dotenv
import os

load_dotenv()


class YouGile:
    def __init__(self, url):
        self.url = url
        self._token = None

    def get_headers(self):
        token = self.get_token()
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def get_token(self):
        token = os.getenv("API_KEY")
        return token

    def create_project(self, title):
        new_project = {
            'title': title
        }
        response = requests.post(self.url + "projects",
                                 json=new_project,
                                 headers=self.get_headers())
        return response

    def get_project_id(self, id_proj):
        response = requests.get(self.url + "projects/" + str(id_proj),
                                headers=self.get_headers())
        return response

    def egit_project(self, id_project, new_title):
        body = {
            'title': new_title
        }
        response = requests.put(self.url + "projects/" + str(id_project),
                                json=body,
                                headers=self.get_headers())
        return response

    def all_projects(self):
        response = requests.get(self.url + "companies*",
                                headers=self.get_headers())
        return response

    def edit_none_token(self, id_proj, new_title, token=None):
        new_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        body = {
            'title': new_title
        }
        response = requests.put(self.url + "projects/" + str(id_proj),
                                json=body,
                                headers=new_headers)
        return response.json()

    def delete_project(self, project_id):
        response = requests.delete(
            f"{self.url}/projects/{project_id}",
            headers=self.get_headers())
        return response
