pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        DOCKER_LOGIN = crednetials('DOCKER_LOGIN')
    }
    stages{
        stage('Testing') {
            sh 'bash scripts/testing.sh'

        }
        stage('Docker Install') {
            sh 'bash scripts/installdocker.sh'
            
        }
        stage('Docker Compose Build') {
            sh 'docker-compose build'
            
        }
        stage('Docker Compose Push') {
            sh 'docker-compose push'
        }
        stage('Docker Compose Up') {
            sh 'docker-compose up'

            
        }
    }
}