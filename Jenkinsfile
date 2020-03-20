def commitCounter = env.BUILD_NUMBER.toInteger()
    
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script{
                    echo "!!!!!~~~~~~~~ commit number: ${commitCounter}"
                    if (commitCounter%2 != 0){
                       error 'Number of commits doesn\'t meet the building criteria!'
                    }
                    //when {equals expected: 15, actual: commitCounter}

                    echo "This's the 8th commit"
                    echo "After ------> ${commitCounter}"
                    sh './mvnw package' 
                }
            }
        }
    }
}