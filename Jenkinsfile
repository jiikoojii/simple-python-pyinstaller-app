pipeline {
    agent { docker { image 'python:latest' }}
    stages {
        stage('Build') { 
                steps {
					sh '''
					pipenv install requests
					python dice.py
					python hello.py
					'''
				}
        }
    }
}
