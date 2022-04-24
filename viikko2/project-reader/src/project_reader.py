from urllib import request
from project import Project
import toml 

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        toml_content = toml.loads(content)   
        project_info = toml_content["tool"]["poetry"]
        # print(toml_content["tool"]["poetry"])
        # print(project_info["name"])
        

        new_project = Project(
            project_info["name"],
            project_info["description"],
            project_info["dependencies"],
            project_info["dev-dependencies"]
        )

        return new_project