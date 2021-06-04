#!/bin/bash

ssh host-1 << EOF

git clone https://github.com/AJBroomfield/practical-project.git

cd practical-project

git checkout feat_nginx 

export DATABASE_URI=${DATABASE_URI}

sudo groupadd docker
sudo usermod -aG docker ${USER}

docker stack deploy --compose-file docker-compose.yaml app

EOF
