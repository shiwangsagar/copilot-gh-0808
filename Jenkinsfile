pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'brainupgrade/copilot-python'
        KUBE_CONTEXT = 'your-kube-context'
        KUBE_NAMESPACE = 'your-namespace'
    }

    stages {


        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

    }
}