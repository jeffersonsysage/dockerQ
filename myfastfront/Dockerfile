#FROM node:latest
#WORKDIR /myfastfront
#COPY . /myfastfront
#RUN npm i
#EXPOSE 3000
#CMD npm start

FROM node:latest as build
WORKDIR /myfastfront
ENV PATH /myfastfront/node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./
RUN npm ci --silent
RUN npm install react-scripts@3.4.1 -g --silent
COPY . /myfastfront/
RUN npm run build
RUN npm install -g serve
CMD serve -s build -l 4000
