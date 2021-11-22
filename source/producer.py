import requests
import time
from source.project import Project, Reader, Singleton


class Producer:
    """ Produz requisição para o pypi """
    def request(self, key: str):
        project = Singleton().__dict__[key]
        res = requests.get(f"https://pypi.org/pypi/{project['packageName']}/json")

        if res.status_code == 200:
            project['latestVersion'] =  res.json()['info']['version']

            if project['currentVersion'] == 'standard':
                project['currentVersion'] = project['latestVersion']

            if project['latestVersion'] == project['currentVersion']:
                project['outOfDate'] = 'false'
            else:
                project['outOfDate'] = 'true'
        else:
            print("Erro na requisição")



