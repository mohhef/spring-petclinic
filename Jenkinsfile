def commitNumber = 0
def successfulSHA = null
def lastSuccessfulHash = null
def didFail = false

pipeline {
    agent any
    stages {
        stage('getCommitNumber') {
          steps{
            script{
              value = readFile('D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\counter.txt').trim()
              commitNumber= value as int
              echo "There are ${commitNumber} commits"
            }
          }
        }
    }
}


