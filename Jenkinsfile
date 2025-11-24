pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python Venv...'
                // Clean slate: Remove old venv if it exists
                sh 'rm -rf env' 
                sh 'python3 -m venv env'
                
                // Install dependencies into the venv
                sh 'env/bin/pip install --upgrade pip'
                sh 'env/bin/pip install -r requirements.txt'
                sh 'env/bin/pip install matplotlib'
            }
        }

        stage('Train & Visualize') {
            steps {
                echo 'Training Model...'
                // Run training inside venv
                sh 'env/bin/python train_model.py'
                
                echo 'Generating Graph...'
                sh 'env/bin/python visualize.py'
            }
        }

        stage('Package Artifact') {
            steps {
                echo 'Zipping the Application...'
                // Create a deployment package
                sh 'zip -r release_package.zip main.py iris_model.pkl requirements.txt'
            }
        }

        stage('Smoke Test API') {
            steps {
                echo 'Starting API in background...'
                script {
                    // 1. Start Uvicorn in background using 'nohup' so it doesn't die
                    // We save the Process ID (PID) to a file so we can kill it later
                    sh 'nohup env/bin/uvicorn main:app --host 0.0.0.0 --port 8001 > api.log 2>&1 & echo $! > pid.txt'
                    
                    // 2. Wait for it to boot
                    sleep 5
                    
                    // 3. Test it
                    echo 'Pinging API...'
                    sh 'curl -v http://localhost:8001/health'
                    
                    // 4. Cleanup: Read the PID and kill the process
                    sh 'kill $(cat pid.txt)'
                }
            }
        }
    }

    post {
        always {
            // Save the Zip and the Plots
            archiveArtifacts artifacts: 'release_package.zip, iris_plot.png, api.log', fingerprint: true
            
            // Cleanup: Ensure no stray python processes are left running
            sh 'rm -f pid.txt'
        }
        success {
            echo 'Pipeline Succeeded (No Docker used)!'
        }
    }
}