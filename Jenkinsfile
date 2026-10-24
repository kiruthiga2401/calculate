pipeline {
    agent any
    
    environment {
        // Unoda Docker Hub username-ai inge podu
        DOCKER_HUB_USER = 'kiruthigakanagaraj'
        IMAGE_NAME      = 'simple-calc'
        IMAGE_TAG       = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                script {
                    sh "docker build -t ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.IMAGE_TAG} ."
                    sh "docker build -t ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:latest ."
                }
            }
        }
        
       stage('Push to Docker Registry') {
    steps {
        echo 'Pushing Image to Docker Hub...'
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
            sh '''
                echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_USERNAME" --password-stdin
                docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}
                docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest
            '''
        }
    }
}
    }
    
    post {
        always {
            echo 'Cleaning up local images...'
            sh "docker rmi ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.IMAGE_TAG} || true"
            sh "docker rmi ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:latest || true"
        }
    }
}
