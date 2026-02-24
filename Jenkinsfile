pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-app .'
            }
        }

        stage('Run Tests Inside Docker') {
            steps {
                bat 'docker run --rm flask-app pytest'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name flask-test flask-app'
            }
        }

        stage('Smoke Test') {
    steps {
        powershell 'Start-Sleep -Seconds 5'
        bat 'curl http://localhost:5000'
    }
}
        stage('Cleanup') {
            steps {
                bat 'docker stop flask-test || exit 0'
                bat 'docker rm flask-test || exit 0'
            }
        }
    }
}
