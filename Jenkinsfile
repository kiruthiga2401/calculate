pipeline {
    agent any
    
    environment {
        DOCKER_HUB_USER = 'kiruthigakanagaraj'
        IMAGE_NAME      = 'simple-calc'
        IMAGE_TAG       = "${BUILD_NUMBER}"
        // Jenkins Credentials-ல உங்க Docker Hub username & password-க்கு 
        // ID ah 'docker-hub-credentials' nu கொடுத்திருக்கீங்களான்னு செக் பண்ணிக்கோங்க
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
        
        Stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker Image to Docker Hub...'
                script {
                    // Jenkins Credentials யூஸ் பண்ணி login பண்றோம்
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
                    // Branch-க்கு தகுந்த மாதிரி Port நிர்ணயம்
                    def hostPort = 5000
                    if (env.BRANCH_NAME == 'production') {
                        hostPort = 6000
                    }

                    def containerName = "${env.IMAGE_NAME}-${env.BRANCH_NAME}"

                    // பழைய container இருந்தால் நிறுத்தி நீக்குவது
                    sh "docker stop ${containerName} || true"
                    sh "docker rm ${containerName} || true"

                    // புதிய container-ஐ சரியான Port-ல் Run செய்வது
                    sh "docker run -d --name ${containerName} -p ${hostPort}:5000 ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.IMAGE_TAG}"
                    
                    echo "Successfully deployed ${env.BRANCH_NAME} on port ${hostPort}"
                }
            }
        }
    }
}
