pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Backend Deps') {
            steps {
                dir('backend') {
                    sh '''
                        echo "===== Building backend image ====="
                        docker build -t backend-test .
                    '''
                }
            }
        }

        stage('Test Backend Import') {
            steps {
                sh '''
                    echo "===== Importing Main.py ====="
                    docker run --rm backend-test python -c "import Main; print('IMPORT OK')"
                '''
            }
        }

        stage('Compose Up') {
            steps {
                sh '''
                    docker compose down || true
                    docker compose build --no-cache
                    docker compose up -d
                    sleep 5
                    echo "===== Container status ====="
                    docker ps -a
                '''
            }
        }

        stage('Smoke Test') {
            steps {
                sh '''
                    echo "===== Backend logs ====="
                    docker logs Backend || true
                    echo "===== Checking backend docs endpoint ====="
                    docker exec Backend python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8000/docs').status)"
                '''
            }
        }
    }

    post {
        always {
            sh 'docker compose down || true'
        }
    }
}
