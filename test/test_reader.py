import pytest
import ast
import json

from source.project import Reader, Singleton


@pytest.fixture
def mocked_projects():
    """ Método que faz mock da leitura do requirements.txt formatando de acordo o que foi especificado """

    json_req = [
        {'packageName': 'pandas', 'currentVersion': '1.3.0', 'latestVersion': '0.0.0', 'outOfDate': 'false'},
        {'packageName': 'numpy', 'currentVersion': '0.0.0', 'latestVersion': '0.0.0', 'outOfDate': 'false'},
        {'packageName': 'redis', 'currentVersion': '3.5.2', 'latestVersion': '0.0.0', 'outOfDate': 'false'},
        {'packageName': 'matplotlib', 'currentVersion': '0.0.0', 'latestVersion': '0.0.0', 'outOfDate': 'false'},
        {'packageName': 'Flask', 'currentVersion': '2.0.0', 'latestVersion': '0.0.0', 'outOfDate': 'false'},
        {'packageName': 'requests', 'currentVersion': '2.25.1', 'latestVersion': '0.0.0', 'outOfDate': 'false'},
        {'packageName': 'uvicorn', 'currentVersion': '0.0.0', 'latestVersion': '0.0.0', 'outOfDate': 'false'},
        {'packageName': 'beautifulsoup4', 'currentVersion': '4.9.1', 'latestVersion': '0.0.0', 'outOfDate': 'false'}
        ]
    

    ##return json.loads(json_req)
    return json_req

def test_reader_ok(mocked_projects):
    
    reader = Reader()
    reader.read(f"requirements.txt")
    
    project_dict = Singleton().__dict__
    mocked_obj = json.dumps(mocked_projects[0])
    assert json.dumps(project_dict['pandas']) == mocked_obj
    


