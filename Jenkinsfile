pipeline {
  agent {
    docker {
      image 'python:3.7.2'
    }
  }
  stages {
    stage('build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pip3 install --user -r requirements.txt'
        }
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'python test.py'
        }
      }
    }
  }
}
