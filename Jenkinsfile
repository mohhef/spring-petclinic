pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat './mvnw clean' 
            }
        }
        stage('Test') {
            steps {
                bat './mvnw test'
            }
        }
        stage('Package') {
            steps {
                bat './mvnw package' 
            }
        }
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                bat './mvnw deploy'
            }
        }
    }
        post {
       // only triggered when blue or green sign
       success {
           slackSend color: 'good', message: 'Passed Build'
       }
       // triggered when red sign
       failure {
           slackSend color: 'bad', message: 'Failed Build'
       }
    }
}
