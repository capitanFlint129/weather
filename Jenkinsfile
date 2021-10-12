pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build --tag tekkengod129/weather:latest .'
        }
      }
    }
    stage('Push') {
      steps {
        withDockerRegistry([ credentialsId: "dockerhub", url: "" ]) {
            sh 'docker push tekkengod129/weather:latest'
        }
      }
    }
  }
}