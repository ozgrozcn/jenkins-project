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


	}


}
