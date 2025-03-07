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
    }

    post {
        success {
            emailext (
                subject: "Jenkins Build Success: ${JOB_NAME} - Build #${BUILD_NUMBER}",
                body: """
                    Build Status: SUCCESS
                    Job: ${JOB_NAME}
                    Build Number: ${BUILD_NUMBER}
                    Check console output at ${BUILD_URL}
                """,
                to: 'i211660@nu.edu.pk'
            )
        }
        failure {
            emailext (
                subject: "Jenkins Build Failed: ${JOB_NAME} - Build #${BUILD_NUMBER}",
                body: """
                    Build Status: FAILURE
                    Job: ${JOB_NAME}
                    Build Number: ${BUILD_NUMBER}
                    Check console output at ${BUILD_URL}
                """,
                to: 'i211660@nu.edu.pk'
            )
        }
    }
}
