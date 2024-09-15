#server login
ssh -i douzo/SSHKEY/SSHKEY01.pem root@160.251.139.45

#git
alias gall='git add -A && git commit -m '''commit''' && git push origin main'

alias build='git pull;docker-compose build;docker-compose up -d'

#logon to container
docker exec -it douzo_app_1 /bin/bash

#check container
docker-compoe ps