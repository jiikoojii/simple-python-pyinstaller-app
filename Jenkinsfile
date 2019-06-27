pipeline {
    agent { docker { image 'python:latest' }}
    stages {
        stage('Build') { 
                steps {
					sh '''
					python hello.py
					ls -la
					ping -c 3 www.google.com
					'''
				}
        }
    }
}
