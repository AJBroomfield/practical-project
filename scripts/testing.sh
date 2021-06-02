#!/bin/bash

sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

#Pytests
python3 -m pytest class-api --cov=app --junitxml=junit/test-results.xml --cov-report.xml
python3 -m pytest race-api --cov=app --junitxml=junit/test-results.xml --cov-report.xml 
python3 -m pytest stat-api --cov=app --junitxml=junit/test-results.xml --cov-report.xml
python3 -m pytest server --cov=app --junitxml=junit/test-results.xml --cov-report.xml
