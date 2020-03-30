def commitNumber = 0

pipeline {
    agent any
    stages {

        stage('getCommitNumber') {
          steps{
            script{
              value = readFile('hello.txt').trim()
              commitNumber= value as int
              echo "The comit number is ${commitNumber}"
            }
          }
        }
    }       
}


