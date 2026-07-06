pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Start Services') {
            steps {
                sh 'docker compose up --build -d'
            }
        }
        stage('Debug Workspace') {
            steps {
                sh '''
                    pwd
                    ls -R
                    ls backend
                '''
            }
}

        stage('Smoke Test') {
            steps {
                sh '''
                    docker ps
                    docker logs Backend
                    docker exec Backend curl -f http://localhost:8000/docs
        '''
            }
        }

        stage('Stop Containers') {
            steps {
                sh 'docker compose down'
            }
        }
    }

    post {
        always {
            sh 'docker compose down || true'
        }
    }
}
