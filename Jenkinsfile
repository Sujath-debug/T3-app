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
        sh 'trivy fs .'
    }
}

        stage('Test') {
            steps {
                sh 'echo Running tests'
            }
        }
stage('Approval') {
    steps {
        input message: 'Approve production deployment?'
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
stage('Approval') {
    steps {
        input message: 'Approve production deployment?'
    }
}
