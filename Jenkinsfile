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
        echo "🔐 Creating Python virtual environment"
        python3 -m venv .venv
        source .venv/bin/activate

        echo "📦 Installing dependencies"
        pip install --upgrade pip
        pip install -r backend/requirements.txt

        echo "🔍 Running Snyk test (strict)"
        snyk test --file=backend/requirements.txt --severity-threshold=high

        echo "📤 Uploading results to Snyk dashboard"
        snyk monitor --file=backend/requirements.txt
        '''
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
