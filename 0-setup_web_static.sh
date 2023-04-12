#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y install nginx

if [ ! -d "/data/web_static/releases/test" ];then
	sudo mkdir -p /data/web_static/releases/test;
    echo "Hello There!" | sudo tee "/data/web_static/releases/test/index.html";
fi

if [ ! -d "/data/web_static/shared/" ];then
	sudo mkdir /data/web_static/shared/;
fi

if [ -h "/data/web_static/current" ];then
	sudo rm -rf /data/web_static/current;
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current;
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current;
fi

sudo chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" | sudo tee /etc/nginx/sites-enabled/default


sudo service nginx restart

exit 0;
