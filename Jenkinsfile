pipeline {
    agent any

    environment {
        SNYK_TOKEN = credentials('snyk-token')
    }

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
                sh '''
snyk test backend --file=backend/requirements.txt --severity-threshold=high                '''
snyk test backend --file=backend/package-lock.json --severity-threshold=high                '''
snyk test backend --file=backend/package.json --severity-threshold=high                '''


            }
        }
        stage('Docker Security Scan') {
    steps {
        sh '''
        snyk test --docker Dockerfile --severity-threshold=high
        '''
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
                echo 'Deploying to production BSML'
            }
        }
    }
}
