pipeline {
    agent any
    
    environment {
        DOCKER_HUB_USER = 'kiruthigakanagaraj'
        IMAGE_NAME      = 'simple-calc'
        IMAGE_TAG       = "${BUILD_NUMBER}"
        // Jenkins Credentials la unoda Docker Hub username & password-ku 
        // ID ah 'docker-hub-credentials' nu kuduthurunu check panniko
        DOCKER_CREDS    = 'docker-hub-credentials'
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
        
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker Image to Docker Hub...'
                script {
                    // Jenkins Credentials use panni login panrom
                    withCredentials([usernamePassword(credentialsId: "${env.DOCKER_CREDS}", 
                                                     usernameVariable: 'DOCKER_USER', 
                                                     passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo '${DOCKER_PASS}' | docker login -u '${DOCKER_USER}' --password-stdin"
                        sh "docker push ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.IMAGE_TAG}"
                        sh "docker push ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:latest"
                    }
                }
            }
        }
        
        stage('Deploy / Run Container') {
            steps {
                echo 'Deploying Container...'
                script {
                    // Munadi run aana old container iruntha athula stop/remove panrom (Port conflict varama irukka)
                    sh "docker stop ${env.IMAGE_NAME} || true"
                    sh "docker rm ${env.IMAGE_NAME} || true"
                    
                    // Puthiya image-ah pull panni, local port 5000-la run panrom (App port-ku etra mathiri change panniko, eg: 80, 5000)
                    sh "docker run -d --name ${env.IMAGE_NAME} -p 6000:5000 ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:latest"
                }
            }
        }
    }
}
