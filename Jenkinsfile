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
            script{
            try{
            bat './mvnw test'
            }
            catch(error){
              didFail=true
            }
            }
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

        stage('saveSuccessfulHash'){
          when{
            expression{didFail == false}
          }
          steps{
          script{
            bat "git rev-parse --short HEAD > D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\successfulSHA.txt"                        
            commit_id = readFile("D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\successfulSHA.txt")
            echo "${commit_id}"
            }
          }
          }

        stage('ifBuildFailed'){
          when{
            expression{didFail == true && commitNumber>=5}
          }
          steps{
            script{
              STABLE = readFile("D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\successfulSHA.txt") 
              bat "git rev-parse --short HEAD > D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\failureSHA.txt"                        
              BROKEN = readFile("D:\\Winter2020\\SOEN345\\Ass\\A6\\spring-petclinic\\failureSHA.txt")

              bat "git bisect start ${BROKEN}${STABLE}"
			        bat "git bisect run mvn clean test"
			        bat "git bisect reset"
            }
          }
        }
    }
}


