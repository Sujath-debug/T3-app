pipeline {
    agent any 
        stages {
            stage ('Install Python Dependencies') {
                steps {
                    echo 'setting up python environment'
                    dir ('backend') {
                                sh 'python3 -m venv venv'
                                sh '. venv/bin/activate && pip install -r requirements.txt'
                 }
             }
            
          }           
}    
}
