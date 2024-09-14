#git
alias gall='git add -A && git commit -m '''commit''' && git push origin main'

alias build='git pull;docker-compose build;docker-compose up -d'

#logon to container
docker exec -it douzo_app_1 /bin/bash

#check container
docker-compoe ps