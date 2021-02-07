pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "docker build . -t recipes_api:latest"
            }
        }
        stage('Run'){
            steps{
                sh "docker run --env-file .env -d -p 5000:5000 recipes_api:latest"
            }
        }
    }
}