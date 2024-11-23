# Data Analytics Application

This repository contains a Python-based data analytics application that has been containerized and deployed using Kubernetes, Minikube, and Jenkins. The project implements a CI/CD pipeline to automate the build, test, and deployment processes.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up Python Environment](#2-set-up-python-environment)
  - [3. Run the Application Locally](#3-run-the-application-locally)
- [Containerization with Docker](#containerization-with-docker)
- [CI/CD Pipeline with Jenkins](#cicd-pipeline-with-jenkins)
- [Kubernetes Deployment with Minikube](#kubernetes-deployment-with-minikube)
- [Testing](#testing)
- [Author](#author)

---

## Overview

This project demonstrates how to:
1. Develop a Python application for data analytics.
2. Containerize the application using Docker.
3. Automate the CI/CD process using Jenkins.
4. Deploy the application to a local Kubernetes cluster using Minikube.
5. Perform automated testing using Pytest.

---

## Technologies Used

- **Version Control**: GitHub
- **Programming Language**: Python
- **Containerization**: Docker
- **CI/CD Tool**: Jenkins
- **Orchestration**: Minikube (Kubernetes)
- **Testing Framework**: Pytest

---

## Project Structure

```plaintext
├── data                   # Contains sample data files
│   └── sample.csv         # Sample CSV data for the application
├── src                    # Source code for the application
│   ├── app.py             # Flask-based web app
│   ├── analysis.py        # Data analysis logic
│   └── utils.py           # Utility functions
├── tests                  # Unit tests
│   └── test_analysis.py   # Pytest-based test for analysis
├── k8s                    # Kubernetes manifests
│   ├── deployment.yaml    # Kubernetes deployment configuration
│   └── service.yaml       # Kubernetes service configuration
├── Dockerfile             # Dockerfile to containerize the application
├── requirements.txt       # Python dependencies
├── Jenkinsfile            # Jenkins pipeline definition
└── README.md              # Documentation
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/BaldeepArora/data-analytics-app.git
cd data-analytics-app
```
### 2. Set Up Python Environment

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependancies
```bash
pip install -r requirements.txt
```
3.  Run the Application Locally

1. Start the Flask application:
```bash
python src/app.py
```
2. Access the application in your browser at http://127.0.0.1:5000.

---

## Containerization with Docker

1. Build the Docker image:
   ```bash
   docker build -t data-analytics-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 data-analytics-app
   ```

---
   
## CI/CD Pipeline with Jenkins

1. **Set Up Jenkins**:
   - Install Jenkins on your machine.
   - Install required plugins (e.g., Docker, GitHub).

2. **Pipeline Definition**:
   - Use the provided `Jenkinsfile` to define the build, test, and deploy stages.

3. **Run the Pipeline**:
   - Configure Jenkins to use this repository and trigger the pipeline.

---

## Kubernetes Deployment with Minikube

1. **Start Minikube**:
   ```bash
   minikube start
   ```
2. **Deploy to Kubernetes:** Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```
3. **Access the Application:** Retrieve the Minikube IP:
   ```bash
   minikube ip
   ```
Access the application at http://<minikube-ip>:<node-port>.

---

## Testing

1. Run unit tests using Pytest:
   ```bash
   pytest tests/
   ```
2. Verify the results to ensure all tests pass.

---

## Author

**Baldeep Arora**  
GitHub: [BaldeepArora](https://github.com/BaldeepArora)

---




