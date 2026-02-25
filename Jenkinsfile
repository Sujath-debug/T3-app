pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building application'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'echo Running security scan'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to production'
            }
        }
    }
}
