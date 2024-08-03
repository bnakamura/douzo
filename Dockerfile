FROM certbot/certbot:v2.11.0

RUN mkdir -p /user/share/nginx/html
RUN mkdir -p /usr/share/nginx/api
RUN mkdir -p /usr/share/nginx/auth

RUN certbot certonly --webroot -w /usr/share/nginx/html --domains="$DOMAIN" --webroot -w /usr/share/nginx/api --domains="$API_NAME" --webroot -w /usr/share/nginx/auth --domains="$KEY_DOMAIN" -m $MAIL --agree-tos