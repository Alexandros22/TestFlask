pipeline {
  agent {
    docker {
      image 'python:3.7.2'
      args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
    }

  }
  stages {
    stage('build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pip install -r requirements.txt'
        }
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }
    }
  }
}
