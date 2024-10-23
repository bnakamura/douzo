
import pytest
from apps.app import create_app

def test_hoge():
    assert 1 == 1 

@pytest.fixture
def app():

    return create_app()

def test_dbs(app):
    
    # 本来は実行前にKeycloakからトークンを取得するのが良い
    token="eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJVQ1NWVUh1cmdRTUl5TWp4bFBDUkliRkpsc00zVEY0MlVpdzdEU3FTMnZFIn0.eyJleHAiOjE3Mjk2Njg0ODksImlhdCI6MTcyOTY2MTI4OSwianRpIjoiYjc3NTI3MGEtZTg4Ni00MzAyLThiOGItZGIxOTM2NDk4ZDEzIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmRvdXpvLnRvcDo4NDQzL3JlYWxtcy9ob2dlcGVrZSIsImF1ZCI6WyJmbGFza3MiLCJhY2NvdW50Il0sInN1YiI6IjliNWFjYmI1LTgwZDYtNDBmNS1hNTJmLTg2YWMzZjM0ZjFmNCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImZsYXNrcyIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLWhvZ2VwZWtlIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIiwiY2xpZW50SWQiOiJmbGFza3MiLCJjbGllbnRIb3N0IjoiMTYwLjI1MS4xMzkuNDUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC1mbGFza3MiLCJjbGllbnRBZGRyZXNzIjoiMTYwLjI1MS4xMzkuNDUifQ.K5K3wRsZ1sQ7uZvyAssGkrdjCFpVoCHZfL7reXXqhB7AvWs-49n-7pniUQDR1WKR9Ff8ZYjLElxwyKXxwldOCMk77a1Na_ez3WtWyE1SSGPmjP8DYZdzuajh4BuEw1VqS-xpsmwzINQji1GKdlek43yTwNC0aoB6mJQdNFALVkiOeK96lLMzJ-C1_abPs4pKq3Nx5uUVuc4jEwBLrGMS1XaiYYHNxfwSPBoG6MVFxjooHf03rqd_oZ1yXFobu9sTkdd20Fv6ozUeFKCD3rwnXl2duNYGLUugzVxDkqSxEdG-lG1kn5arCI96_uwCZxI_Zry42Im0rTzTe-327k_Qnw"

    app.config['TESTING'] = True
    # getの場合
    response = app.test_client().get('/api/v1/dbs', headers={'X-Access-Token': token})
    # postの場合
    # app.test_client().post('/dashboard', 
    # data=dict(hoge='1111', peke='2222'),
    # headers={'content-md5': 'some hash'})
    print(response.data)
    app.logger.debug(response.data)
    body = response.get_json()
    print(body)

    # ひとまずsystem_idのみテストを行う
    assert body['money']['system_id'] == "3b07be22-fa23-450f-bd73-79439922b1bb"
    # Web画面は現状認証が入っているとテストが大変なので、認証を外した状態でテストすると良いです。