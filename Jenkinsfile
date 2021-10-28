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
        stage('Deploy to K8s') {
            steps {
                sshagent(['k8s-master']) {
                    sh 'scp -r -o StrictHostKeyChecking=no deployment.yaml root@94.26.239.10:/kubernates'
                    script {
                        try {
                            sh 'ssh root@94.26.239.10 kubectl apply -f /kubernates/deployment.yaml --kubeconfig=/root/.kube/config'
                        } catch(error) { }
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