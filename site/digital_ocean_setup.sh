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
&& sudo apt install -y docker-ce \
&& mkdir -p /src \
&& cd /src \
&& git clone https://github.com/jsal13/sneakbike.git \
&& cd sneakbike/site \
&& docker build -t sneakbike . \
&& docker run -d -p 8080:8081 sneakbike \

