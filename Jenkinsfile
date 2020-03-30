def commitNumber = 0
def resetNumber=0
def successfulSHA = null
def commitHashForBuild( build ) {
  def scmAction = build?.actions.find { action -> action instanceof jenkins.scm.api.SCMRevisionAction }
  return scmAction?.revision?.hash
}
def lastSuccessfulHash = null
def lastSuccessfulBuild = currentBuild.rawBuild.getPreviousSuccessfulBuild()

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
        stage('getSuccessfulSHA'){
          steps{
            script{
              value = readFile('D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\successfulSHA.txt').trim()
              successfulSHA = value
              echo "The SHA file is ${successfulSHA}"
            }
          }
        }
        stage('doFullBuild'){
          when{
            expression{commitNumber>=5 || successfulSHA==''}
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
            bat "py writeToFile.py"
          }
        }

        stage('getSuccessfulHash'){
          steps{
          script{
            Id = bat (returnStdout: true, script: "git rev-parse HEAD").trim()
            }
          }
          }
    }
}


