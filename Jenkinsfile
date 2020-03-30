def commitNumber = 0
def resetNumber=0

pipeline {
    agent any
    stages {

        stage('getCommitNumber') {
          steps{
            script{
              value = readFile('counter.txt').trim()
              commitNumber= value as int
              echo "There are ${commitNumber} commits"
            }
          }
        }

        stage('doFullBuild'){
          when{
            expression{commitNumber>=5}
          }
          steps{
            bat './mvnw clean'
          }
        }

        stage('resetCommitNumber'){
          when{
            expression{commitNumber>=5}
          }
          steps{
            bat "py writeToFe.py"
          }
        }

    }       
}


