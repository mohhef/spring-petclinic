def =${env.JOB_NAME}
def job = hudson.model.Hudson.instance.getItem(jobname)
def builds = job.getBuilds()

def thisBuild = builds[0]
def fourBuildsAgo = builds[4] 

println('env' + builds[0].getEnvironment().keySet() )
println('each job has previous job e.g "' + thisBuild.getPreviousBuild() + '"')

fourBuildsAgo.getChangeSets().each {
  println('Num of commits in this build ' + (it.getLogs()).size() )

  it.getLogs().each {
     println('commit data : '  + it.getRevision() + ' ' + it.getAuthor() + ' ' + it.getMsg()) 
  }
}


