#!/usr/bin/env bash
#Bash script to setup a web server

sudo apt update
sudo apt upgrade -y
sudo apt install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

string=\
"server {
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
}
"
echo "$string" | sudo tee /etc/nginx/sites-enabled/default

service nginx restart
