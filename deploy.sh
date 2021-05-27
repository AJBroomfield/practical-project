#!/bin/bash

# build server
docker build -t practical_project_server server

# build class-api
docker build -t practical_project_class_api class-api

# build stat-api
docker build -t practical_project_stat_api stat-api

# build race-api
docker build -t practical_project_race_api race-api

# create network
docker network create practical_project_network

# run containers

docker run -d -p 5000:5000 --name practical_project_server --network practical_project_network practical_project_server
docker run -d --name class_api --network practical_project_network practical_project_class_api 
docker run -d --name race_api --network practical_project_network practical_project_race_api
docker run -d --name stat_api --network practical_project_network practical_project_stat_api