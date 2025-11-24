pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python Venv...'
                // REMOVED: apt-get commands (We don't need them anymore)
                
                sh 'rm -rf env' 
                sh 'python3 -m venv env'
                
                sh 'env/bin/pip install --upgrade pip'
                sh 'env/bin/pip install -r requirements.txt'
                sh 'env/bin/pip install matplotlib'
            }
        }

        stage('Train & Visualize') {
            steps {
                echo 'Training Model...'
                sh 'env/bin/python train_model.py'
                
                echo 'Generating Graph...'
                sh 'env/bin/python visualize.py'
            }
        }

        stage('Package Artifact') {
            steps {
                echo 'Packaging the Application...'
                // FIX: Use 'tar' (Standard Linux tool) instead of 'zip'
                // -c: Create, -z: Gzip (Compress), -f: File
                sh 'tar -czf release_package.tar.gz main.py iris_model.pkl requirements.txt'
            }
        }

        stage('Smoke Test API') {
            steps {
                echo 'Starting API in background...'
                script {
                    sh 'nohup env/bin/uvicorn main:app --host 0.0.0.0 --port 8001 > api.log 2>&1 & echo $! > pid.txt'
                    sleep 5
                    echo 'Pinging API...'
                    sh 'curl -v http://localhost:8001/health'
                    sh 'kill $(cat pid.txt)'
                }
            }
        }
    }

    post {
        always {
            // UPDATE: Archive the .tar.gz file instead of .zip
            archiveArtifacts artifacts: 'release_package.tar.gz, iris_plot.png, api.log', fingerprint: true
            sh 'rm -f pid.txt'
        }
        success {
            echo 'Pipeline Succeeded (Green)!'
        }
    }
}