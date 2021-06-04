#!/bin/bash

ssh nginx << EOF

rm -rf practical-project/

git clone https://github.com/AJBroomfield/practical-project.git

cd practical-project

git checkout feat_nginx

sudo groupadd docker
sudo usermod -aG docker ${USER}

cd nginx

docker-compose up -d

EOF
