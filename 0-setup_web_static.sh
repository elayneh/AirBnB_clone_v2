#!/usr/bin/env bash
# server setup to deployment

apt-get update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
sudo echo "<html>
  <head>
  </head>
  <body>
    ALX School
  </body>
</html>" > | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

new_location="\tserver_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\}\n"

sudo sed -i "s-\tserver_name _;-$new_location-" /etc/nginx/sites-available/default
sudo sed -i "s-\tserver_name _;-$new_location-" /etc/nginx/sites-enabled/default
sudo service nginx restart