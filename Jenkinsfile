pipeline {
    agent any

    stages {
        
        stage('1. Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('2. Run Tests') {
            steps {
                bat 'pytest'
            }
        }
        
        stage('3. Deploy') {
            steps {
                echo 'Build exitoso'
            }
        }
    }
}