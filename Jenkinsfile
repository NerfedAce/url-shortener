pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/NerfedAce/url-shortener.git'
            }
        }

        stage('Build & Start Services') {
            steps {
                sh 'docker compose up --build -d'
            }
        }

        stage('Smoke Test') {
            steps {
                sh '''
                    sleep 30
                    curl -f http://localhost:8000/docs || exit 1
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
