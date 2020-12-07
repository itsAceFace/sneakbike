FROM node:15.3.0-buster

WORKDIR /src

COPY . .
RUN npm i
RUN npm i -g @vue/cli

CMD ["npm", "run", "serve"]
