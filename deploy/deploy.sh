#!/bin/sh
#NOTE: This script is designed to be run on a fresh Ubuntu 14.04 install.
#      If you run it on a server that has an installed webserver, it may fail.
#      If you run it on a server that is not running Ubuntu 14.04, it may fail.
#      If you run it on a server used for other tasks, it may fail (or break
#       the other programs on that server).

#NOTE: This script will deploy a production instance of the airbnb clone.
#      The production version of the airbnb_clone requires two environmental
#      variables to be set: AIRBNB_ENV should contain "production" and
#      AIRBNB_DATABASE_PWD_PROD should contain the database password, unless
#      you want to hardcode them in config.py. Which you probably shouldn't do.

#update!
apt-get update
apt-get upgrade -y

#install necessary dependencies
apt-get install nginx gunicorn git python-pip python-dev -y
pip install flask flask-json peewee

#configure nginx
echo `cat <<NGINX_DEFAULT_SERVER_AIRBNB_CONFIG
server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    server_name _;
    location / {
        proxy_pass http://localhost:3000;
    }
}
NGINX_DEFAULT_SERVER_AIRBNB_CONFIG` > /etc/nginx/sites-available/airbnb_api

#enable api
ln -s /etc/nginx/sites-available/airbnb_api /etc/nginx/sites-enabled/default
service nginx start

# deploy airbnb clone
cd /opt/
# get api code
git clone https://github.com/johnserrano/airbnb_clone.git

#run gunicorn
cd airbnb_clone/api
gunicorn --bind 0.0.0.0:3000 wsgi:app
