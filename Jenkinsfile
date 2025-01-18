pipeline {
    agent any

    environment {
            REMOTE_SERVER = 'root@10.101.169.172' // 替换为你的远程用户名和IP或域名
            JEN_PATH = '/var/jenkins_home/workspace/testpython'
            SER_PATH = '~/myjenkins/mypython'
        }

    stages {
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
               
                sh "ssh ${REMOTE_SERVER} 'rm -rf ${SER_PATH}/*'"
                // 上传文件到服务器
                sh "scp ${JEN_PATH}/* ${REMOTE_SERVER}:${SER_PATH}"

                sh "ssh ${REMOTE_SERVER} 'bash ${SER_PATH}/jenkins.sh'"
            }
        }
    }

    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
    }
}
