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
	      stage('test') {
		      steps{
		      echo 'Unit Test is applying'
		      sh 'echo "Results are correct"'
	              echo 'Unit Test is done'
		      echo 'Funtctional Test is applying'
		      echo 'Functional Test is done'
		      }
	      }
	      stage('monitor') {
		      steps{ 
		      	echo 'Date detection'
			sh 'python condition.py'
			sh 'ls -l'
			echo "OS INFORMATIONS:"
			sh '''			
			cat /etc/os-release
			'''
			echo "STORAGE:"
			sh '''
			df -h
			'''
			echo "RAM USAGE:"
			sh '''
			sudo yum update -y
			sudo yum install free -y
			free -h
			'''
			echo 'Finished' 
		      }
	      }
	}


	
}
