FROM certbot/certbot:v2.11.0

RUN mkdir -p /usr/share/nginx/html
RUN mkdir -p /usr/share/nginx/api
RUN mkdir -p /usr/share/nginx/auth

#RUN certbot certonly --webroot -w /usr/share/nginx/html --domains="$DOMAIN" --webroot -w /usr/share/nginx/api --domains="$API_NAME" --webroot -w /usr/share/nginx/auth --domains="$KEY_DOMAIN" -m bnakamur@hotmail.com --agree-tos --register-unsafely-without-email

RUN certbot certonly --standalone --webroot --webroot-path /usr/share/nginx/html -d "$DOMAIN" --webroot --webroot-path -w /usr/share/nginx/api -d "$API_NAME" --webroot --webroot-path -w /usr/share/nginx/auth -d "$KEY_DOMAIN" -m bnakamur@hotmail.com --agree-tos --non-interactive