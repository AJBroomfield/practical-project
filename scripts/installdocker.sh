#!/bin/bash


sudo apt update
sudo apt install -y curl jq

#Install docker
curl https://get.docker.com | sudo bash

#Install docker-compose
sudo apt update
sudo apt install -y curl jq

version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose

#Docker login
docker login -u $DOCKER_LOGIN_USR-p $DOCKER_LOGIN_PSW


