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

# トークンが有効か確認する
curl -k
-X POST
-u "flasks:G6xqdoC33HytUhEi0vjvUgKMSGZ2QXYL"
-d "token=$TOKEN"
"https://auth.douzo.top:8443/realms/hogepeke/protocol/openid-connect/token/introspect"