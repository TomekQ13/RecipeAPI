pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                docker-compose up --build
            }
        }
        stage('Stop') {
            steps {
                docker-compose down
            }
        }
    }
}