pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo "✅ Jenkins is working!"
                sh 'ls -la'
                sh 'git log -1 --oneline'
            }
        }
    }
    post {
        always {
            echo "🏁 Build finished (status update skipped for testing)"
        }
    }
}
