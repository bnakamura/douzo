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
docker-compoe ps

#mysql login -u の後にユーザ名、-pの後に空白無しでパスワード
mysql -u hogehoge -phogehoge

#DataBase 表示
show databases;

#使用するDBの選択
use hoge;

#存在するテーブルの表示
show tables;

#テーブル構造の表示
show create table money;