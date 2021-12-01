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
                   args '-u=\"root\"'
                  }}
    steps{
      sh 'apk add --update python3 py-pip'
      sh 'pip install Flask'
      sh 'pip install xmlrunner'
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
