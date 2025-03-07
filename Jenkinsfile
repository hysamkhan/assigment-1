pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'hysam/assigment-1' // Your Docker Hub image name
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hysamkhan/assigment-1.git'
            }
        }

        stage('Check Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} -t ${DOCKER_IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh """
                            docker logout || true  # Ensure no existing session causes issues
                            echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin
                            sleep 5  # Wait for login to fully take effect
                        """
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh """
                        docker push ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE_NAME}:latest
                    """
                }
            }
        }

        stage('Logout from Docker Hub') {
            steps {
                sh "docker logout || true"
            }
        }

        stage('Send Email Notification') {
            steps {
                script {
                    emailext subject: "Jenkins Build Notification: ${JOB_NAME} - Build #${BUILD_NUMBER}",
                        body: """
                        <p><strong>Build Status:</strong> ${CURRENT_BUILD_RESULT}</p>
                        <p><strong>Project:</strong> ${JOB_NAME}</p>
                        <p><strong>Build Number:</strong> ${BUILD_NUMBER}</p>
                        <p><strong>Build URL:</strong> <a href="${BUILD_URL}">${BUILD_URL}</a></p>
                        """,
                        to: "i211660@nu.edu.pk",
                        from: "i211660@nu.edu.pk",
                        replyTo: "i211660@nu.edu.pk",
                        mimeType: 'text/html'
                }
            }
        }
    }
}
