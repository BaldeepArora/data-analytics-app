pipeline {
    agent any  // Run on any available Jenkins agent
    stages {
        stage('Build') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests using pytest
                    bat 'pytest tests/'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    docker.build('my-python-app:latest')
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy application using kubectl
                    bat 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
