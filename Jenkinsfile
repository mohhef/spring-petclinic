def commitNumber = 0
def resetNumber = 0

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
            script{
              writeFile file: "hello.txt", text: "This file is useless, no need to archive it."
            }
          }
        }

    }       
}


