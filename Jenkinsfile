pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Abhivox/Flask-Jenkins-CI.git'
            }
        }

        stage('Create Virtual Env') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest'
            }
        }
    }
}
