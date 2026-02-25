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
    environment {
        SNYK_TOKEN = credentials('snyk_token')
    }
    steps {
        sh '''
        docker run --rm \
          -e SNYK_TOKEN=$SNYK_TOKEN \
          -v "$PWD:/project" \
          -w /project \
          snyk/snyk:docker snyk test --severity-threshold=high
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
