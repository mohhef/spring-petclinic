def commitNumber = 0

pipeline {
    agent any
    stages {

        stage('getCommitNumber') {
          steps{
            script{
              value = readFile('hello.txt').trim()
              commitNumber= value as int
              echo "There are ${commitNumber} commits"
            }
          }
        }

        state('doFullBuild'){
          when{
            expression{commitNumber>=5}
          }
          steps{
            bat './mvnw clean compile'
          }
        }
        
    }       
}


