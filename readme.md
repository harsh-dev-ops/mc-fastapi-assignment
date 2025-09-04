# MC Fastapi Assignment

## Project Setup
- Clone the project
    ```sh
    git clone 
    ```

- Change directory
    ```sh
    cd mc_fastapi_assignment
    ```

- Docker Build
    1. Dev Image Build
        ```sh
        docker build . -f docker/dockerfile.dev -t accounts_app:dev
        ```

    2. Test Image Build
        ```sh
        docker build . -f docker/dockerfile.test -t accounts_app:test
        ```

    3. Prod Image Build
        ```sh
        docker build . -f docker/dockerfile.prod -t accounts_app:prod
        ```

- Docker Image Run
    1. Run dev image
        ```sh
        docker run -p 8000:80 accounts_app:dev
        ```

    2. Run prod image
        ```sh
        docker run -p 8001:80 accounts_app:prod
        ```

    3. Run Test image
        ```sh
        docker run accounts_app:test
        ```

-  Image build and run using docker compose
    1. Build all images
        ```sh
            docker compose build 
        ```

    2. Run app (development)
        ```sh
            docker compose up dev_app
        ```

    3. Run test cases
        ```sh
            docker compose up test_app
        ```

## API Documentation
**Postman**
https://documenter.getpostman.com/view/15907649/2sB3HkpKhQ

**Swagger API Documentation**
- after running the application visit http://localhost:8000/docs

## Code Modifications and Corrections
**Create Account API**
- Created a seperate POST request api to maintain the seperation of concern of create and update.

**Update Account API**
- PATCH api to update the content of a account.

**Delete Account API**
- Fixed bug in delete account api

**Code refactoring**
- Added fastapi's inbuilt status codes for better readability.
- Custom Exceptions to implement DRY principle.
- Modulation of code for future extensions.

## Test Cases
**Pytest**
- Implemented pytest with async client of fastapi app. 
- Removes the dependency of running the api first to test them.
- Api testing can happen without running the application.
- Covered all the edge cases for 4 apis.
- Wrote total 9 test cases including health check api.

## Dockerfiles
**DEV**
- Created a seperate docker files for devs, so that do development inside the container.
- Used python:3.13-slim for development (as dev are most familar with ubuntu environment)
- Exposed port was 80
- Local machine port would be 8000
- Seperation of dev and prod image will ensure, dev changes should happen in the dockerfile.dev not in the dockerfile.prod.

**TEST**
- Create a test docker file to do the testing for locally as well in CI of the application.
- No port is exposed
- Can run easily using docker compose

**PROD**
- Created a python:3.13-alpine image for production.
- Implemented Healthcheck
- Added user in runtime so that, no one can't install anything in the running container.


## Future Scope
**Github Action for CI**
- We can integerate the CI with github actions, so that CI part that include code linting, building of docker image, testing it and pushing to container registry happens using gitOps.

**Jenkins for CI**
- We can setup jenkins runner, to build CI pipeline that includes linting, building of docker image, testing it and pushing to container registry.
- Jenkins runner setup can be done in 3 ways: Linux/MacOS runners, jenkins running inside docker container, jenkins runner with kubernetes.
- To build image with kubernetes jenkins runner, we will have to use Kaniko.

**Kubernetes Cluster**
- For seamless orchestration we can use kubernetes, it can also help us to manage stagging and prod enviroments by using different namespaces.
- Jenkins runner can also run inside kuberenetes cluster.

**ArgoCD for CD**
- CD can be manage by ArgoCd, we need a seperate manifest repository for that to update image tags in yaml deployment files after CI process.
- CI process will have to update the content of the yaml file after pushing the docker image in container registry.
- Stagging stage should be added before merging and deploying to production.
- To setup ArgoCd there is a simple documentation on argoCD platform.

**Database**
- API needs databases to store the data permanently. 
- We can choose any SQL or NoSQL database to store the data.

**API Caching**
- To handle high traffic, api caching should be implemented.
- We can use redis for that.

**Rate Limiting**
- To eliminate exhaustion of resources by bots we can use API Rate Limiting.


## Conclusion
- As per current requirement and code, api's can run successfully.
- Api versioning is also included for future extensions.
- Test cases will ensure CI and code refactoring, developers will be able to tackle any code changes using that.
- Apline image for prod will ensure the smaller image size, so that orchestors can deploy the new image immediately.