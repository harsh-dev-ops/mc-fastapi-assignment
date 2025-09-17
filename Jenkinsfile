pipeline {

  agent {
    kubernetes {
      yamlFile 'k8s/jenkins-containers.yaml'
    }
  }

  environment {
    APP_NAME     = "mc-fastapi-assignment"
    RELEASE      = "1.0.0"
    DOCKER_USER  = "harsh8383"
    DOCKER_PASS  = 'dockerhub'
    IMAGE_NAME   = "${DOCKER_USER}/${APP_NAME}"
    IMAGE_TAG    = "${RELEASE}-${BUILD_NUMBER}"
    /* JENKINS_API_TOKEN = credentials("JENKINS_API_TOKEN") */
  }

  stages {

    stage("Cleanup Workspace") {
      steps {
        cleanWs()
      }
    }

    stage("Checkout from SCM") {
      steps {
        git branch: 'dev', credentialsId: 'github', url: 'https://github.com/harsh-dev-ops/mc-fastapi-assignment'
      }
    }

    stage('Kaniko: Build & Push the test image') {
      steps {
        container(name: 'kaniko', shell: '/busybox/sh') {
          sh """
            #!/busybox/sh
            /kaniko/executor --dockerfile `pwd`/docker/dockerfile.prod --context `pwd` --destination=${IMAGE_NAME}:${IMAGE_TAG} --destination=${IMAGE_NAME}:latest
          """
        }
      }
    }

    // stage('Kubernetes: Pull & Test the app') {
    //   steps {
    //       sh "curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.23.0/bin/linux/amd64/kubectl"
    //       sh "chmod +x ./kubectl"

    //       sh "./kubectl delete pod/${APP_NAME}-test -n jenkins --ignore-not-found=true"

    //       sh """
    //         ./kubectl run ${APP_NAME}-test \
    //         -n jenkins \
    //         --image=${IMAGE_NAME}:${IMAGE_TAG} \
    //         --command -- python3 -m pytest
    //         """

    //       sleep 180

    //       // Wait for completion
    //       // sh "./kubectl wait --for=condition=Ready pod/${APP_NAME}-test -n jenkins --timeout=60s || true"
    //       // sh "./kubectl wait --for=condition=ContainersReady pod/${APP_NAME}-test -n jenkins --timeout=60s || true"
    //       // sh "./kubectl wait --for=condition=Complete pod/${APP_NAME}-test -n jenkins --timeout=120s || true"

    //       // Get logs
    //       echo "=== TEST OUTPUT ==="
    //       sh "./kubectl logs -n jenkins ${APP_NAME}-test"

    //       sh "./kubectl delete pod/${APP_NAME}-test -n jenkins --ignore-not-found=true --timeout=30s"
    //   }
    // }

    stage("Kubectl: Pull & Test the app"){
      steps {
        container('kubectl') {
           sh "kubectl delete pod/${APP_NAME}-test -n jenkins --ignore-not-found=true"

          sh """
            kubectl run ${APP_NAME}-test \
            -n jenkins \
            --image=${IMAGE_NAME}:${IMAGE_TAG} \
            --command -- python3 -m pytest
            """

          // sleep 180

          // Wait for completion
          sh "kubectl wait --for=condition=Ready pod/${APP_NAME}-test -n jenkins --timeout=60s || true"
          sh "kubectl wait --for=condition=ContainersReady pod/${APP_NAME}-test -n jenkins --timeout=60s || true"
          sh "kubectl wait --for=condition=Complete pod/${APP_NAME}-test -n jenkins --timeout=120s || true"

          // Get logs
          echo "=== TEST OUTPUT ==="
          sh "kubectl logs -n jenkins ${APP_NAME}-test"

          sh "kubectl delete pod/${APP_NAME}-test -n jenkins --ignore-not-found=true --timeout=30s"
        }
      }
    }
  }
}
