FROM certbot/certbot:v1.21.0

RUN mkdir -p /usr/share/nginx/html
RUN mkdir -p /usr/share/nginx/api
RUN mkdir -p /usr/share/nginx/auth

#RUN certbot certonly --webroot -w /usr/share/nginx/html --domains="$DOMAIN" --webroot -w /usr/share/nginx/api --domains="$API_NAME" --webroot -w /usr/share/nginx/auth --domains="$KEY_DOMAIN" -m bnakamur@hotmail.com --agree-tos --register-unsafely-without-email

RUN certbot certonly --standalone -w /usr/share/nginx/html -d "$DOMAIN" -w /usr/share/nginx/api -d "$API_NAME" -w /usr/share/nginx/auth -d "$KEY_DOMAIN" -m bnakamur@hotmail.com --agree-tos