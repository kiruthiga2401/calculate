pipeline {
    agent any
    
    environment {
        // Unga Docker Hub username matrum Image name-a inge maathunggal
        DOCKER_HUB_USER = 'your_dockerhub_username'
        IMAGE_NAME      = 'simple-calc'
        IMAGE_TAG       = "${BUILD_NUMBER}" // Jenkins build number-a tag-a vechikrom
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                // Git repo-vil irundhu code-a edukum
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                script {
                    // Dockerfile vechu image build pannudhu
                    sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                    sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest ."
                }
            }
        }
        
        stage('Push to Docker Registry') {
            steps {
                echo 'Pushing Image to Docker Hub...'
                // Jenkins Credentials Manager-la 'docker-hub-credentials' nu ID vechu user/pass save panni irukanum
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                    sh "echo \$DOCKER_HUB_PASSWORD | docker login -u \$DOCKER_HUB_USERNAME --password-stdin"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up local images...'
            // Server tools space consume aagama iruka local storage build images-a remove pannidhum
            sh "docker rmi ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} || true"
            sh "docker rmi ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest || true"
        }
    }
}
