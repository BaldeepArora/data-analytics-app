pipeline {
    agent any  // Run on any available Jenkins agent

    environment {
    KUBECONFIG = 'C:\\ProgramData\\Jenkins\\.jenkins\\.minikube\\config'
    }


    stages {

        stage('Verify Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Verify Pip') {
            steps {
                bat 'pip --version'
            }
        }


        stage('Debug PATH') {
            steps {
                bat 'echo %PATH%'
            }
        }
 

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
                    docker.build('data-analytics-app:latest')
                }
            }
        }
        
        stage('Verify Kubernetes Auth') {
            steps {
                bat 'kubectl get nodes'
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
