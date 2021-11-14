pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'COMMIT=$(git rev-parse --verify HEAD)'
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
                        docker push tekkengod129/weather:latest
                    '''
                }
            }
        }
        stage('Deploy to K8s') {
            steps {
                sshagent(credentials: ['k8s-master']) {
                    script {
                        sh 'ssh root@94.26.239.10 "kubectl set image deployments/weather-deployment weather=tekkengod129/weather:${COMMIT}"'
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
