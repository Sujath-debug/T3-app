pipeline {
    agent any 
        stages {
            stage ('build') {
                steps {
                    echo 'Getting Dependeicies'
                    dir ('backend') {
                                sh 'pip3 install --user -r requirements.txt'
                 }
             }
            
          }           
}    
}
