#!/bin/bash

ssh host-1 << EOF

git clone https://github.com/AJBroomfield/practical-project.git

cd practical-project

git checkout feat_ansible 

export DATABASE_URI=${DATABASE_URI}

docker stack deploy --compose-file docker-compose.yaml app

EOF