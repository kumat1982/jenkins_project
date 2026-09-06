pipeline {
    agent any

    stages {
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
