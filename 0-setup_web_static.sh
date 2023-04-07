#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

if [ ! -d "/data/" ];then
    sudo mkdir /data/;
fi

if [ ! -d "/data/web_static/" ];then
    sudo mkdir /data/web_static/;
fi

if [ ! -d "/data/web_static/releases/" ];then
	sudo mkdir /data/web_static/releases/;
fi

if [ ! -d "/data/web_static/shared/" ];then
	sudo mkdir /data/web_static/shared/;
fi

if [ ! -d "/data/web_static/releases/test/" ];then
	sudo mkdir "/data/web_static/releases/test/";
	echo "Hello There!" | sudo tee "/data/web_static/releases/test/index.html";
fi

if [ -h "/data/web_static/current" ];then
	sudo rm -rf /data/web_static/current;
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current;
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current;
fi

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i 's/server_name _\;/server_name _\;\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/\;\n\t}\n/g' /etc/nginx/sites-enabled/default

sudo service nginx restart
