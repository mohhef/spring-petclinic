def commitNumber = 0
def successfulSHA = null
def lastSuccessfulHash = null
def didFail = false
def forSureBROKEN=null

pipeline {
    agent any
    stages {

        stage('getCommitNumber') {
          steps{
            script{
              value = readFile('D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\counter.txt').trim()
              commitNumber= value as int
              echo "There are ${commitNumber} commits in total"
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

        stage('doFullBuildClean'){
          when{
            expression{commitNumber>=8 || successfulSHA==''}
          }
          steps{
            script{
            try{
            bat './mvnw Clean'
            }
            catch(error){
              didFail=true
            }
            }
          }
        }

        stage('doFullBuildTest'){
          when{
            expression{commitNumber>=8 || successfulSHA==''}
          }
          steps{
            script {
            try{
            bat './mvnw test'
            echo "${didFail}"
            }
            catch(error){
              didFail=true
              echo "${didFail}"
            }
            }
          }
        }

        stage('doFullBuildPackage'){
          when{
            expression{(commitNumber>=8 || successfulSHA=='') && didFail==false}
          }
          steps{
            script{
            try{
            bat './mvnw package'
            }
            catch(error){
              didFail=true
            }
            }
          }
        }

        stage('saveSuccessfulHash'){
          when{
            expression{didFail == false}
          }
          steps{
          script{
            bat "git rev-parse --short HEAD > D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\successfulSHA.txt"                        
            commit_id = readFile("D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\successfulSHA.txt")
            echo "Passing build is ${commit_id}"
            }
          }
        }

        stage('ifBuildFailed'){
          when{
            expression{didFail == true && commitNumber>=8}
          }
          steps{
            script{
              if(successfulSHA != ''){
                STABLE = readFile("D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\successfulSHA.txt")
                bat "git rev-parse --short HEAD > D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\failureSHA.txt"                        
                BROKEN = readFile("D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\failureSHA.txt").trim()
                bat "git bisect start ${BROKEN} ${STABLE}"
                bat "git bisect run ./mvnw clean test"
                bat "git bisect reset"
              }else{
                bat "git rev-parse --short HEAD > D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\failureSHA.txt"                        
                forSureBROKEN = readFile("D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\failureSHA.txt").trim()
              }
            }
          }
        }

        stage('resetCommitNumber'){
          when{
            expression{commitNumber>=8 && forSureBROKEN == null}
          }
          steps{
            bat "py writeToFile.py"
          }
        }
       }
}


