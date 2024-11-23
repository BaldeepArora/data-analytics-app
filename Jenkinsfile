pipeline {
    agent any  // Run on any available Jenkins agent
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests using pytest
                    sh 'pytest tests/'
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
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
