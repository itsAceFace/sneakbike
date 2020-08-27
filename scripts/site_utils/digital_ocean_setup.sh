# Run this script on a clean droplet, ubuntu:18.04
sudo apt update \
&& sudo apt install -y \
    vim \
    curl \
    git \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
&& curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash - \
&& sudo apt-get install -y nodejs \
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
&& sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" \
&& sudo apt update \
&& sudo apt install -y docker-ce nginx \
&& mkdir -p /src \
&& cd /src \
&& git clone https://github.com/jsal13/sneakbike.git \
&& cd sneakbike/site \
&& docker build -t sneakbike . \
&& docker run -d -p 8000:8080 sneakbike \
&& sudo echo "
server {
  listen        80;
  listen        [::]:80 default_server;
  server_name   sneakbikemysteryrace.com;

  location / {
    proxy_pass  http://localhost:8000;
  }
}" | sudo tee /etc/nginx/sites-available/default \
&& sudo systemctl restart nginx
