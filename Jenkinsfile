pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build --tag tekkengod129/weather:latest .'
            }
        }
        stage('Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        usernameVariable: 'DOCKERHUB_USERNAME',
                        passwordVariable: 'DOCKERHUB_PASSWORD',
                        credentialsId: 'dockerhub'
                    )
                ]) {
                    sh '''
                        docker login --username $DOCKERHUB_USERNAME --password $DOCKERHUB_PASSWORD
                        docker push tekkengod129/weather:latest
                    '''
                }
            }
        }
    }
}