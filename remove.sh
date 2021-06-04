#!/bin/bash

docker rm -f $(docker ps -qa)
docker rmi practical_project_race_api:latest practical_project_stat_api:latest practical_project_class_api:latest practical_project_server:latest 
docker network rm practical_project_network 
