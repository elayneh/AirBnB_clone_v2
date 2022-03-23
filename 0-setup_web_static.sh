#!/usr/bin/env bash
# set up web server for deployment

apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdie -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo '<html>
  <head>
  </head>
  <body>
    This is the content for the html file to test if it is created
  </body>
</html>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/release/test/ /data/web_static_current
chown -hR ubuntu:ubuntu /data
sed -i '51 i \\n\tlocation /hbnt_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
service nginx restart
