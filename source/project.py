from typing import List
import json
import re
import requests
import time

from source.singleton import Singleton

class Reader:
    """ Classe  responsável por ler o arquivo de requirementes e formata-lo com o formato JSON """

    
    re_specific_version = re.compile(".+[>=]{1,2}.+")

    re_standard_version = re.compile(".+\[standard\]")

    def place_version(self, project: str) -> List[str]:
        """  Lê um projeto com nome e versão e retorna  uma lista formatada"""
        if not self.re_specific_version.match(project):
            if self.re_standard_version.match(project):
               project =  project.replace("[standard]", "== standard")
            else:
                project = project + "== standard" 
        
        return project.replace('\n', '').replace("==", ",").replace(">=", ",").split(",")


    def read(self, path: str):
        dict_packages = {}
        singleton = Singleton()

        with open(path, "r") as reader:
            for line in reader:
                if line != '\n': 
                    replaced_line = self.place_version(line)
                    project = Project(replaced_line[0].strip(), replaced_line[1].strip())
                    dict_packages[replaced_line[0].strip()] = project.__dict__
                    singleton = Singleton(dict_packages)  

        ##return singleton


class Project(object):
    """Representa o object que será transformado em JSON de acordo com a especificação """
    def __init__(self, packageName, currentVersion, latestVersion="0.0.0", outOfDate="false"):
        self.packageName = packageName
        self.currentVersion = currentVersion
        self.latestVersion = latestVersion
        self.outOfDate = outOfDate

    def __str__(self):
        return json.dumps(self.__dict__)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.packageName:
            raise StopIteration
        return self
    
