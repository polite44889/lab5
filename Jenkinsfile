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
   
    steps{
      sh 'phyton3 tested_app.py'
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
