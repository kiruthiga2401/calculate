pipeline {
    agent any
    
    environment {
        // ⚠️ Inga unoda real Docker Hub username-ai podu (e.g., 'kiruthigakanagaraj')
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
                // Jenkins credentials ID 'docker-hub-credentials' nnu correct-ah irukkanum
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                    // Fix: Fixed variable mapping syntax so it uses the actual credential username
                    sh "echo '${env.DOCKER_HUB_PASSWORD}' | docker login -u '${env.DOCKER_HUB_USERNAME}' --password-stdin"
                    sh "docker push ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.IMAGE_TAG}"
                    sh "docker push ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:latest"
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
