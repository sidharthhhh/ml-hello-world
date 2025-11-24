pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "iris-ml-api"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Creating Virtual Environment...'
                // 1. Create venv named 'env'
                // 2. Upgrade pip inside the venv
                // 3. Install requirements inside the venv
                sh '''
                    python3 -m venv env
                    env/bin/pip install --upgrade pip
                    env/bin/pip install -r requirements.txt
                    env/bin/pip install matplotlib
                '''
            }
        }

        stage('Train Model') {
            steps {
                echo 'Training the Model...'
                // Use the python INSIDE the venv (env/bin/python)
                sh 'env/bin/python train_model.py'
            }
        }

        stage('Generate Reports') {
            steps {
                echo 'Creating Visualizations...'
                // Use the python INSIDE the venv
                sh 'env/bin/python visualize.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                // Docker doesn't care about the venv, it builds from the Dockerfile
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Test Container') {
            steps {
                echo 'Smoke Testing...'
                sh "docker run -d -p 8000:8000 --name ml-test-${BUILD_NUMBER} ${DOCKER_IMAGE}:${DOCKER_TAG}"
                sleep 5
                sh "curl -f http://localhost:8000/health"
                sh "docker rm -f ml-test-${BUILD_NUMBER}"
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'iris_model.pkl, iris_plot.png', fingerprint: true
        }
        success {
            echo 'Pipeline Succeeded.'
        }
        failure {
            echo 'Pipeline Failed.'
        }
    }
}