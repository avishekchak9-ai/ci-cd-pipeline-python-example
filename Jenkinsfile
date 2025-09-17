// Jenkinsfile for Python Flask Application

pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "python-flask-app"
        DOCKER_IMAGE_TAG = "${env.BUILD_NUMBER}"
        APP_PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Install Dependencies & Lint') {
            steps {
                echo "Installing dependencies..."
                script {
                    docker.image('python:3.9-slim-buster').inside('-u root') {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo "Running unit tests..."
                script {
                    docker.image('python:3.9-slim-buster').inside('-u root')  {
                        sh 'pip install -r requirements.txt'
                        sh 'python3 -m unittest test_app.py'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                script {
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ."
                    sh "docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ${DOCKER_IMAGE_NAME}:latest"
                }
            }
        }

        stage('Run Docker Container (Local Test)') {
            steps {
                echo "Running application in Docker container..."
                script {
                    // Stop and remove any existing container of the same name to avoid conflicts
                    sh "docker ps -a --filter 'name=my-flask-app' --format '{{.ID}}' | xargs -r docker stop"
                    sh "docker ps -a --filter 'name=my-flask-app' --format '{{.ID}}' | xargs -r docker rm"

                    // Run the new container
                    sh "docker run -d -p ${APP_PORT}:${APP_PORT} --name my-flask-app ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
                    sleep 5 // Give it a moment to start up
                }
            }
        }
    }
    post {
        success {
            echo "Pipeline succeeded! App is running at http://localhost:${APP_PORT}"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
