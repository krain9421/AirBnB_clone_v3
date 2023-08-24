#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static.

# Install Nginx if not already installed
sudo apt update -y
sudo apt install nginx -y

# Create required directories if they don't exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create fake index.html file
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tTesting Nginx Configuration\n\t</body>\n</html>" >/data/web_static/releases/test/index.html

# Create the symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Add alias to serve the content of /data/web_static/current to hbnb_static
sudo sed -i '51i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart the nginx service
service nginx restart
