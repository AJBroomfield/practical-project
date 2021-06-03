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

        stage('Ansible') {
            steps {
                sh 'bash scripts/ansible.sh'
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
                sh 'bash scripts/deploy.sh'
            }
            

            
        }
    }
    post{
        always{
            perfReport filterRegex: '', showTrendGraphs: true, sourceDataFiles: '**/*.xml'
        }
    }
}