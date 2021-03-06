pipeline {
    agent any
    environment {
       COMMIT = (sh (script: "git rev-parse --short HEAD", returnStdout: true)).trim()
    }
    stages {
        stage('Build') {
            steps {
                sh '''
                    docker image build . \
                      -t "tekkengod129/weather:latest" \
                      -t "tekkengod129/weather:${COMMIT}"
                '''
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
                        docker push tekkengod129/weather:${COMMIT}
                        docker push tekkengod129/weather:latest
                    '''
                }
            }
        }
        stage('Deploy to K8s') {
            steps {
                withKubeConfig([credentialsId: 'kubernetes-token', serverUrl: 'https://weather.p5.do-school.ru:6443']) {
                    sh 'kubectl set image deployments/weather-deployment weather=tekkengod129/weather:${COMMIT}'
                }
            }
        }
    }
    post {
        always {
            sh 'docker logout'
            cleanWs()
        }
    }
}
