# QA - Practical Project - Random DnD Character

## **Contents**
* [Introduction](#introduction)
   + [Requirements](#requirements)
   + [My Solution](#my-solution)
* [Architecture](#architecture)
  + [Planning](#planning)
  + [Risk Assessment](#risk-assessment)
  + [Database](#database)
  + [Service Diagram](#service-diagram)
* [Continuous Integration](#continuous-integration) 
  + [CI Pipeline](#ci-pipeline)
  + [Testing](#testing)
  + [Jenkins](#jenkins)
  + [Docker](#docker)
  + [Ansible](#ansible)
  + [NGINX](#nginx)
* [Review](#review)
  + [Future Improvements](#future-improvements)
  + [Scrum Review](#scrum-review)
* [Author](#review)
* [Acknowledgements](#acknowledgements) 

## **Introduction**
### **Requirements**
The aim of this project is to:
> Create a service-orientated architecture for your application, 
> this application must be composed of at least 4 services that work together.

This projects had some constraints and required the forllowing technologies to be implemented.
>  * Kanban Board: Asana or an equivalent Kanban
>  * Version Control: Git
>  * CI Server: Jenkins
>  * Configuration Management: Ansible
>  * Cloud Server: GCP Virtual Machines
>  * Containerisatgion: Docker
>  * Orchestration Tool: Docker Swarm
>  * Reverse Proxy: NGINX

### **My Solution**
I decided to make an application which generated a random DnD character and produced its starting ability scores. However, the main focus of this project was the CI (continuous integration) and CD (continuous deployment) so an accurate and clear understanding of the CI pipeline is vital. 

#### **Application** 
* Service 1: Face of the application which displays the object created from service 4
* Service 2: Randomly chooses a race from a list
* Service 3: Randomly chooses a class from a list
* Service 4: Rolls ability scores, assignes the highest value to the most used ability based on class, and add race and class bonuses 

## **Architecture**

### **Planning**
A Trello board was used to visualise user stories and help plan the development of this application by turning it into a smaller tasks. Each of these tasks had MoSCoW prioritisation applied and labelled 'Must Have' were necessary for the minimum viable product. 

![TRELLO_1](https://i.imgur.com/ulPmMs1.jpg)

Each task seen in the product backlog was moved in to the sprint backlog as each of these task were required for MVP. As the each task was started and completed, it moved across the Trello board until it became the definition of done. 

![TRELLO_2](https://i.imgur.com/50KYWvI.jpg)

The image above shows the state of the Trello at the end of the first sprint. The next sprint would invovle further development of the code with the features seen in the product backlog. 

To see the trello in full click [here](https://trello.com/b/knlsmKrM/dnd-character-creator)


### **Risk Assessment**

Before starting this project, I completed a risk assessment covering the risks which could occur when completing this project.

![RISK](https://i.imgur.com/juhNHJY.jpg)

As project was in development an additional risk was discovered as I understood docker framework to a greater detail. This risk is highlighted in grey. 
Each risk required a description, evaluation, likelihood, impact level, responsibility, response, and control measures. As the project went through its development cycle each risk was considered and their control measures were followed.

### **Database**
The database integration for this application is very simple, as it only required a single table. This table will contain all the information generated from the three background services. The diagram below shows its structure.

![ERD](https://i.imgur.com/ViIOPQZ.jpg)


### **Service Diagram**
This project required four services linking together. My application follows the strcuture shown below. 

![SERVICE_DI](https://i.imgur.com/iFwjohT.jpg)

* Service 1: Sends a post request to service 4 and adds the result to an SQL database running on a seperate VM
* Service 2: Generates a random DnD race when sent a GET request
* Service 3: Generates a random DnD class when sent a GET request
* Service 4: When sent a POST request it generates ability scores based on the information it is sent.

## **Continuous Integration**
### **CI Pipeline**

![CI_PIPELINE](https://i.imgur.com/Zvuq8JT.jpg)

The diagram above shows the continuous integration pipeline used for this application. It shows the different stages of development, testing and deployment.

### **Testing**
Testing on this application was done using pytest. These units tests covered the four differents services and tested them with different scenarios. As these services required a random elements, a patch function was used to set these functions to a predetermined value. Another key function which used was the Mock function to simulate the GET and POST request for the service one.  

![TEST_RESULT](https://i.imgur.com/uaP3Dyv.jpg)

The image above shows the result of running the code

 > python3 -m pytest --cov=app --cov-report=term-missing

Each test had a missing terms in each file which correlated to the image below. 

![TEST_MISS](https://i.imgur.com/Akndtgc.jpg)


### Jenkins

### Docker

### Ansible

### NGINX

## Review

### Future Improvements

### Scrum Review

## Author

## Acknowledgements


