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
        sh '''
        echo "🔧 Setting up Python environment"
        python3 -m venv .venv
        source .venv/bin/activate

        pip install --upgrade pip
        pip install -r backend/requirements.txt

        echo "Build completed"
        '''
    }
}

      stage('Security Scan') {
    steps {
        sh '''
        source .venv/bin/activate

        echo "🔍 Python: Snyk strict test"
        snyk test --file=backend/requirements.txt --severity-threshold=high

        echo "📤 Python: upload to Snyk dashboard"
        snyk monitor --file=backend/requirements.txt

        echo "🔍 Node.js: Snyk strict test"
        snyk test --file=backend/package.json --severity-threshold=high

        echo "📤 Node.js: upload to Snyk dashboard"
        snyk monitor --file=backend/package.json
        '''
    }
}
       stage('IaC Security Scan (Dockerfile)') {
    steps {
        sh '''
        echo "🔍 Scanning Dockerfile as Infrastructure-as-Code"
        snyk iac test Dockerfile --severity-threshold=high
        snyk iac monitor Dockerfile
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
