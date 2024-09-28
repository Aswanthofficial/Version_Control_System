pipeline{
  agent any
  triggers{
    githubPush()
  }
  stages{
    stage('Checkout'){
      steps{
        //checkout repository
        checkout scm
      }
    }
  }
}
