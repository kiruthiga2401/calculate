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
    }
}
