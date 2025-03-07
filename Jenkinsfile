pipeline {
    agent any

    stages {
        stage('Pull Code from GitHub') {
            steps {
                git branch: 'master', url: 'https://github.com/hysamkhan/assigment-1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t hysam/mlops-app:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push hysam/mlops-app:latest'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker stop mlops-app || true'
                sh 'docker rm mlops-app || true'
                sh 'docker run -d -p 5001:5000 --name mlops-app hysam/mlops-app:latest'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed!'
        }
    }
}
