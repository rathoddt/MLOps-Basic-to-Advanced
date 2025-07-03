pipeline{
    agent any

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'git-token', url: 'https://github.com/rathoddt/MLOps-Basic-to-Advanced.git']])
                }
            }
        }
    }
}    