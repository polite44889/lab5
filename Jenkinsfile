pipeline {
    agent none
    stages {
        stage('build') {
            agent { docker { image 'alpine' } }
            steps {
                echo '123'
            }
        }
    }
}
