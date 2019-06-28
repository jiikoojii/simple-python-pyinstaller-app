pipeline {
    agent { docker { image 'python:latest' }}
    stages {
        stage('Build') { 
                steps {
					sh '''
					#python dice.py
					python hello.py
					'''
				}
        }
    }
}
