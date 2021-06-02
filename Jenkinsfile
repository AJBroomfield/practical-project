pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        DOCKER_LOGIN = credentials('DOCKER_LOGIN')
    }
    stages{
        stage('Testing') {
            steps {
                sh 'bash scripts/testing.sh'
            }
        }

        stage('Docker Install') {
            steps { 
                sh 'bash scripts/installdocker.sh'
            }
        }
        stage('Docker Compose Build') {
            steps {
                sh 'docker-compose build'
            }  
        }
        stage('Docker Compose Push') {
            steps {
                sh 'docker-compose push'
            }            
        }
        stage('Docker Compose Up') {
            steps {
                sh 'docker-compose up -d'
            }
            

            
        }
    }
}