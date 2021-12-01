pipeline{
  options {timestamps()}

  agent none
  stages {
    stage('Check scm'){
      agent any
      steps{
        checkout scm
      }

    }


  stage('Build'){
    steps{
      echo "Building ...${BUILD_NUMBER}"
      echo "Build complete"
    }
  }
  stage('Test'){
    agent{ docker {image 'python:3'
                   
                  }}
    steps{
      sh 'sudo pip3 install Flask'
      sh 'sudo pip3 install xmlrunner'
      sh 'python3 tested_app.py'
    }
    post{
      always{
        junit 'test-reports/*.xml'
      }
      success{
        echo "Aplication testing successfully complete"
      }
      failure{
        echo "Ooops"
      }
    }
  }
 }
}
