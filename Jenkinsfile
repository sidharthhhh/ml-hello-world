pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "iris-ml-api"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Installing Dependencies...'
                // In real prod, use a Docker agent with Python pre-installed
                sh 'pip install -r requirements.txt' 
                sh 'pip install matplotlib' // Needed for visualization step
            }
        }

        stage('Train Model') {
            steps {
                echo 'Training the Model...'
                // This runs the math and creates 'iris_model.pkl'
                sh 'python train_model.py'
            }
        }

        stage('Generate Reports') {
            steps {
                echo 'Creating Visualizations...'
                // This creates 'iris_plot.png'
                sh 'python visualize.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image with new Model...'
                // The Dockerfile copies the 'iris_model.pkl' we just created above
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Test Container') {
            steps {
                echo 'Smoke Testing...'
                // 1. Run container in background
                sh "docker run -d -p 8000:8000 --name ml-test ${DOCKER_IMAGE}:${DOCKER_TAG}"
                
                // 2. Sleep to let server start
                sleep 5
                
                // 3. Curl the Health endpoint
                sh "curl -f http://localhost:8000/health"
                
                // 4. Cleanup
                sh "docker rm -f ml-test"
            }
        }
    }

    post {
        always {
            // MLOPS GOLD: Archive the Model and Graph
            // This lets you download the model/graph directly from Jenkins UI
            archiveArtifacts artifacts: 'iris_model.pkl, iris_plot.png', fingerprint: true
        }
        success {
            echo 'Pipeline Succeeded. New Model Built.'
        }
        failure {
            echo 'Pipeline Failed.'
        }
    }
}