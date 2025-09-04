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


