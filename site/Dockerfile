FROM ubuntu:18.04

RUN apt update \
    && apt install -y \
    vim \
    curl \
    git \
    software-properties-common \
    && curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs

RUN mkdir -p /src
WORKDIR /src
COPY sneakbike .
RUN npm i

CMD ["npm", "run", "serve"]

