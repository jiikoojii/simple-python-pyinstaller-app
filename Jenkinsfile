pipeline {
    agent { docker { image 'python:latest' }}
    stages {
        stage('Build') { 
                steps {
					sh '''
					python hello.py
					ls -la
					'''
				}
        }
    }
}
