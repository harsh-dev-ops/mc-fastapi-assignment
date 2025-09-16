pipeline {

  agent {
    kubernetes {
      yamlFile 'k8s/kaniko-builder.yaml'
    }
  }

  environment {
        APP_NAME = "mc-fastapi-assignment"
        RELEASE = "1.0.0"
        DOCKER_USER = "harsh8383"
        DOCKER_PASS = 'dockerhub'
        IMAGE_NAME = "${DOCKER_USER}" + "/" + "${APP_NAME}"
        IMAGE_TAG = "${RELEASE}-${BUILD_NUMBER}"
        /* JENKINS_API_TOKEN = credentials("JENKINS_API_TOKEN") */

    }

  stages {

    stage("Cleanup Workspace") {
      steps {
        cleanWs()
      }
    }

    stage("Checkout from SCM"){
            steps {
                git branch: 'dev', credentialsId: 'github', url: 'https://github.com/harsh-dev-ops/mc-fastapi-assignment'
            }
        }

    stage('Kaniko: Build & Push the test image') {
      steps {
        container(name: 'kaniko', shell: '/busybox/sh') {
          sh """
          #!/busybox/sh

            /kaniko/executor --dockerfile `pwd`/docker/dockerfile.prod --context `pwd` --destination=${IMAGE_NAME}:${IMAGE_TAG}
          """
        }
    }
    }

    stage('Kubernetes: Pull & Test the app') {
        steps {
            container('kubectl'){
                sh """
                kubectl run ${APP_NAME} --image=${IMAGE_NAME}:${IMAGE_TAG} --command python3 -m pytest
            """
            }
        }
    }

    stage('Kaniko: Build & Push the Production Image'){
        steps {
        container(name: 'kaniko', shell: '/busybox/sh') {
          sh '''#!/busybox/sh
            /kaniko/executor --dockerfile `pwd`/docker/dockerfile.prod --context `pwd` --destination=${IMAGE_NAME}:latest
          '''
        }
    }

      }
    }
}
