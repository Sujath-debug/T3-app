pipeline {
    agent any 
        stages {
            stage ('print Bismillah') {
                steps {
                    echo 'Iam testing the connection'
                    sh 'whoami'
                    sh 'pwd'
                 }
             }
            stage ('List workspace Files') {
                steps {
                    sh 'ls -la'
                }
            }
          }           
}        
