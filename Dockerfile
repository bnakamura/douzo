FROM certbot/certbot:v2.11.0

RUN certbot certonly -d $DOMAIN -d $API_NAME -d $KEY_DOMAIN -m $MAIL --agree-tos --webroot -w /usr/share/nginx/html
