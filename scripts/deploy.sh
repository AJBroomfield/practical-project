#!/bin/bash

ssh host-1 << EOF

rm -rf practical-project

git clone https://github.com/AJBroomfield/practical-project.git

cd practical-project 

export DATABASE_URI=${DATABASE_URI}

sudo groupadd docker
sudo usermod -aG docker ${USER}

docker stack deploy --compose-file docker-compose.yaml app

EOF
