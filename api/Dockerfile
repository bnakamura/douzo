FROM python:3.10.6-bullseye

# Time Zone
# タイムゾーン、ロケール設定
ENV TZ="Asia/Tokyo" \
    LANG="C.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="C.UTF-8"

# upgrade pip
RUN apt-get update && apt-get install -y \
    && pip install --upgrade pip

RUN apt install -y logrotate
COPY ./inf/uwsgi_log_rotate.conf /etc/logrotate.d/

# appsディレクトリapp.pyのcreate_app()
# Flaskオブジェクトを作成する関数を指定する
ENV FLASK_APP=apps.app:create_app()
ENV FLASK_DEBUG=1

# mysql
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV JWT_PUBLIC_KEY=${JWT_PUBLIC_KEY}
ENV CLIENT_SECRET=${CLIENT_SECRET}

RUN mkdir -p /home/douzo/api

# change dir
WORKDIR /home/douzo/api

# install module
COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt

# 起動
CMD uwsgi --ini app.ini