# QA - Practical Project - Random DnD Character

## Contents
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

## Introduction
### Requirements
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

### My Solution
I decided to make an application which generated a random DnD character and produced its starting ability scores. However, the main focus of this project was the CI (continuous integration) and CD (continuous deployment) so an accurate and clear understanding of the CI pipeline is vital. 

#### Application 
* Service 1: Face of the application which displays the object created from service 4
* Service 2: Randomly chooses a race from a list
* Service 3: Randomly chooses a class from a list
* Service 4: Rolls ability scores, assignes the highest value to the most used ability based on class, and add race and class bonuses 

## Architecture

### Planning

### Risk Assessment

### Database

### Service Diagram

## Continuous Integration

### CI Pipeline

### Testing

### Jenkins

### Docker

### Ansible

### NGINX

## Review

### Future Improvements

### Scrum Review

## Author

## Acknowledgements


