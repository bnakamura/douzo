#git sample
https://github.com/yk-st/udemy-flask-sample/blob/main/commands.md

#server login
ssh -i douzo/SSHKEY/SSHKEY01.pem root@160.251.139.45

#git
alias gall='git add -A && git commit -m '''commit''' && git push origin main'

alias build='git pull;docker-compose build;docker-compose up -d'

#logon to container
docker exec -it douzo_app_1 /bin/bash

#loging to mysql container
docker exec -it mysql_koz /bin/bash

#check container
docker-compose ps

#mysql login -u の後にユーザ名、-pの後に空白無しでパスワード
mysql -u hogehoge -phogehoge
mysql -u root -phogehoge

#DataBase 表示
show databases;

#使用するDBの選択
use hoge;

#存在するテーブルの表示
show tables;

#テーブル構造の表示
show create table money;

#テーブルデータの照会
select * from hoge.money;

#keycloak login
user: admin
pass: hogepeke

# keycloak
SSO session idle timeout変更

# サインアウト(Oauth2proxyからサインアウトしてその後にKeyCloakのサインアウト画面に遷移する)
https://douzo.top/oauth2/sign_out?rd=https%3A%2F%2Fauth.douzo.top%3A8443%2Frealms%2Fhogepeke%2Fprotocol%2Fopenid-connect%2Flogout/

# JWTデコードするためのキー
export JWT_PUBLIC_KEY=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhWcxlmluBu8ZMcafoc2bogOoEXGtsFMax362C3Vkt5F5JCLOJkvUD24vd+1kLpNeI+0pGBuNj7RLK4po3MwdtUc15EJNzJhDFkzDKW6PCj00YWRVkmnLQuCuqP8fvcYNkxXA0J1MdtXkGlujIycwV0v6bI/xpV3iBHBmHHsbD7iUOWZtlt34JFJvDA39coMGZzUEYpqvZZi2jS+wCQIO44plpezwfZSQ97F6lzr4wJ8fFiJK9/w1d68uSe5H/XOTk1r7CskYk7boJeTlJYSVa4BQMBPcXUQHLcHCNffU8swySsEswcWdwjwD6+O+IYHohaNNNDvwBKfDZBAvyDHuUwIDAQAB

# logの参照
# アプリのコンテナにログインして
cat uwsgi.log

# ファイウの容量確認
# アプリのコンテナにログインして
du -h
dh -h

# 返却したいJSON
{
    "resource": {
        "id": "aaa",
        "address": {
            "zip": "peke",
            "postal": "maruo"
        },
        "addresses": [
            {
                "id": 1,
                "zip": "peke",
                "postal": "maruo"
            },
            {
                "id": 2,
                "zip": "pekeo",
                "postal": "maruo2"
            }
        ]
    }
}

# トークン取得系のコマンド
# client_id,client_secretはkeycloakで取得したもの secret.cmd参照
curl -k -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "grant_type=client_credentials&scope=openid" \
-d "client_id=flasks" \
-d "client_secret=FTGlrDWUCvLdmnq44X9yMAewe7jBj2y7" \
"https://auth.douzo.top:8443/realms/hogepeke/protocol/openid-connect/token"


export TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJVQ1NWVUh1cmdRTUl5TWp4bFBDUkliRkpsc00zVEY0MlVpdzdEU3FTMnZFIn0.eyJleHAiOjE3MjgyNjY4NzAsImlhdCI6MTcyODI1OTY3MCwianRpIjoiOTc5MmZlOWMtYTBlZi00NjMxLTg3MzctOTAzN2U5MzQwNGE4IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmRvdXpvLnRvcDo4NDQzL3JlYWxtcy9ob2dlcGVrZSIsImF1ZCI6WyJmbGFza3MiLCJhY2NvdW50Il0sInN1YiI6IjliNWFjYmI1LTgwZDYtNDBmNS1hNTJmLTg2YWMzZjM0ZjFmNCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImZsYXNrcyIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLWhvZ2VwZWtlIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIiwiY2xpZW50SWQiOiJmbGFza3MiLCJjbGllbnRIb3N0IjoiMTYwLjI1MS4xMzkuNDUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC1mbGFza3MiLCJjbGllbnRBZGRyZXNzIjoiMTYwLjI1MS4xMzkuNDUifQ.Wsm1iRRNYPknIbDxW0QKDFgRxxs3AwQialG5udO_RRsb9sgk-nY-d9cH_GqZ4WNAp_v7SXyrzN-ncsT53HqRNCPGnkgdqzAofHBHBYfLYJKZSMpR0OZB5-lNe3jONpBOcBX4erQg2eLLSabVVOMeL21z1P600nYl6_ARvSJ3zl1Lo1w41TyOcwBiSxFkL7tiLZh8AYCT5T7FgEK9F0tPzaVs4N-o7gXgSWyly7qNhN1xPIH0Tby0f2vqLRWy0VPhMdbHKgL1jSwDElwUmHvIzwPhjOL4SE-wgWH5BiwCp-t7-wJBdSFgyVtSp86OAd1nPT7bgdHyooST4UIsezilyQ

# トークンが有効か確認する
curl -k
-X POST
-u "flasks:G6xqdoC33HytUhEi0vjvUgKMSGZ2QXYL"
-d "token=$TOKEN"
"https://auth.douzo.top:8443/realms/hogepeke/protocol/openid-connect/token/introspect"

# flask securityのサイト XSS CSRF
https://runebook.dev/ja/docs/flask/security/index