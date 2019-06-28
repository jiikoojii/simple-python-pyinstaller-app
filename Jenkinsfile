pipeline {
    agent { docker { image 'python:latest' }}
    stages {
        stage('Build') { 
                steps {
					sh '''
					sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
					test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
					test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
					test -r ~/.profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
					echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
					brew install pipenv
					pipenv install requests
					python dice.py
					python hello.py
					'''
				}
        }
    }
}
