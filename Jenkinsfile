pipeline {
   agent any 
      stages {
	stage('build') {
		steps {
			echo 'Pipeline started'
			sh 'python hello-world.py'
			sh 'python loops.py'
			echo 'Pipeline finished'
			}

		}
	stage('deploy'){
		steps{
			echo 'Deployment process is starting..'
			sh 'python loops.py'
			sh 'echo "Connecting to server..."'
			sh 'echo "Codes are deployed"'
			}
		}


	}


}
