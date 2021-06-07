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
  + [NGINX](#nginx)
* [Front End](#front-end)
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

This project had some constraints and required the following technologies to be implemented.
>  * Kanban Board: Asana or an equivalent Kanban
>  * Version Control: Git
>  * CI Server: Jenkins
>  * Configuration Management: Ansible
>  * Cloud Server: GCP Virtual Machines
>  * Containerisation: Docker
>  * Orchestration Tool: Docker Swarm
>  * Reverse Proxy: NGINX

### **My Solution**
I decided to make an application which generated a random DnD character and produced its starting ability scores. However, the focus of this project was the CI (continuous integration) and CD (continuous deployment) so an accurate and clear understanding of the CI pipeline is vital. 

#### **Application** 
* Service 1: Face of the application which displays the object created from service 4
* Service 2: Randomly chooses a race from a list
* Service 3: Randomly chooses a class from a list
* Service 4: Rolls ability scores, assigns the highest value to the most used ability based on class, and add race and class bonuses 

## **Architecture**

### **Planning**
A Trello board was used to visualise user stories and help plan the development of this application by turning steps into a smaller tasks. Each of these tasks had MoSCoW prioritisation applied and labelled 'Must Have' were necessary for the minimum viable product. 

![TRELLO_1](https://i.imgur.com/ulPmMs1.jpg)

Each task seen in the product backlog was moved in to the sprint backlog as each of these tasks were required for MVP. As the each task was started and completed, it moved across the Trello board until it became the definition of done. 

![TRELLO_2](https://i.imgur.com/50KYWvI.jpg)

The image above shows the state of the Trello at the end of the first sprint. The next sprint would involve further development of the code with the features seen in the product backlog. 

To see the trello in full click [here](https://trello.com/b/knlsmKrM/dnd-character-creator)


### **Risk Assessment**

Before starting this project, I completed a risk assessment covering the risks which could occur when completing this project.

![RISK](https://i.imgur.com/juhNHJY.jpg)

As project was in development an additional risk was discovered as I understood docker framework to a greater detail. This risk is highlighted in grey. 
Each risk required a description, evaluation, likelihood, impact level, responsibility, response, and control measures. As the project went through its development cycle each risk was considered and their control measures were followed.

### **Database**
The database integration for this application is quite simple, as it only required a single table. This table will contain all the information generated from the three background services. The diagram below shows its structure.

![ERD](https://i.imgur.com/ViIOPQZ.jpg)


### **Service Diagram**
This project required four services linking together. My application follows the structure shown below. 

![SERVICE_DI](https://i.imgur.com/iFwjohT.jpg)

* Service 1: Sends a post request to service 4 and adds the result to an SQL database running on a separate VM
* Service 2: Generates a random DnD race when sent a GET request
* Service 3: Generates a random DnD class when sent a GET request
* Service 4: When sent a POST request it generates ability scores based on the information it is sent.

## **Continuous Integration**
### **CI Pipeline**

![CI_PIPELINE](https://i.imgur.com/Zvuq8JT.jpg)

The diagram above shows the continuous integration pipeline used for this application. It shows the various stages of development, testing and deployment.

### **Testing**
Testing on this application was done using pytest. These units tests covered the four different services and tested them with different scenarios. As these services required a random element, a patch function was used to set these functions to a predetermined value. Another key function which used was the Mock function to simulate the GET and POST request for the service one.  

![TEST_RESULT](https://i.imgur.com/uaP3Dyv.jpg)

The image above shows the result of running the code

 > python3 -m pytest --cov=app --cov-report=term-missing

Each test had a missing line in each file which correlated to the image below. 

![TEST_MISS](https://i.imgur.com/Akndtgc.jpg)


### **Jenkins**
In my CI pipeline I used Jenkins as my CI server which acts as one of the main cores of the process. Jenkins allows me to set up a pipeline which automatically pulls from the main branch in my git repository and runs the 'Jenkinsfile', in  which contains the breakdown of the of the pipeline job. 

![JENKINS](https://i.imgur.com/9Ra6JZh.jpg)

The steps of the Jenkinsfile are shown above
1. Testing - Runs pytest on each of the four services 
2. Ansible - Sets up VMs making sure required software is installed. Also initialises the docker swarm and connects workers to the manager
3. Docker Install - Ensures docker-compose is installed on the Jenkins machine
4. Docker Compose Build - Builds the images required for the docker swarm 
5. Docker Compose Push - Pushes the built images to dockerhub
6. Docker Swarm Deploy - Run docker stack deploy 
7. Start NGINX - SSH into a separate VM and runs a docker-compose.yaml to create and external container which connects to the swarm

The form of this Jenkins file went through different iterations during development. To correctly test if docker and docker-compose worked with this application. The deployment went through three different deployment steps. 
The first version ran from a simple bash script which set up a docker network, built the images and deployed them. 
The second one created was done using a docker-compose file which converted this deploy script in an easy to understand file which can be then utilised later in the project. 
The third version is what you can see above and was built on these previous two steps. 

### **NGINX**
NGINX acts as a reverse proxy which means it can direct internet traffic from its own IP address and send it to the docker nodes which are contained in the swarm. The inclusion of this service allows the incoming traffic to the application to be split among the docker nodes. It also means that the front end user is isn't directly interacting with application which improves the overall security of the application.
The diagram below summarises NGINX's role in this application

![NGINX](https://i.imgur.com/GBAodOm.jpg)

## **Front End**

![FRONT](https://i.imgur.com/XxW2AVJ.jpg)

The diagram above shows the structure of the front end. This straightforward design was created using Jinja2 templating and allows for the use of input variables which allows me to display the new character roll and import information from an external SQL database which is hosted on GCP.


## Review

### Future Improvements
The current version of this application is the result of the first scrum where the MVP requirements are met. 
If more time were available the following process would be investigated and improved:
* Reduce the time for Jenkins to go through the pipeline and update the task. 
   * Use Jenkins plugins which could help reduce downtime
   * Integrate bash conditionals which could check if a process has already been completed
* Improve the UI of the front-end so the user experience is more unique

### Scrum Review
There were no major problems during this scrum. However, the progress could have been documented better with the integration of assigning story points to tasks which would allow a burndown chart to be created to easily document the rate of progress. 


## Author

Andrew Broomfield

## Acknowledgements

QA DevOps Training Staff


