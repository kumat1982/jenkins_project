pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                sh 'https://github.com/kumat1982/jenkins_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -it myapp:latest '
            }
        }
    }
}
