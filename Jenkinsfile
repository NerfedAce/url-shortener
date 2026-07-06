pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Debug Workspace') {
            steps {
                sh '''
                echo "===== Workspace ====="
                pwd
                ls -R

                echo "===== Backend ====="
                ls -l backend

                echo "===== Dockerfile ====="
                cat backend/Dockerfile

                echo "===== Requirements ====="
                cat backend/requirements.txt
                '''
            }
        }

        stage('Build Images') {
            steps {
                sh '''
                docker compose down || true
                docker compose build --no-cache
                '''
            }
        }

        stage('Test Backend Import') {
            steps {
                sh '''
                echo "===== Importing Main.py ====="

                docker run --rm url-shortener-ci-cd-backend python - <<'EOF'
import traceback

try:
    import Main
    print("SUCCESS: Main imported successfully")
except Exception:
    traceback.print_exc()
    raise
EOF
                '''
            }
        }

        stage('Start Services') {
            steps {
                sh '''
                docker compose up -d
                docker ps -a
                '''
            }
        }

        stage('Smoke Test') {
            steps {
                sh '''
                echo "===== Backend Logs ====="
                docker logs Backend || true

                echo "===== Curl ====="
                curl -f http://localhost:8000/docs
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
            sh '''
            docker compose down || true
            '''
        }
    }
}
