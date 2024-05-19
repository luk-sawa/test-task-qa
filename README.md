# test-task-qa
### Recruitment task to build an automated test suite for a RESTful API

##### Implemented
* RESTful API server exposing four endpoints according to swagger documentation.
* Automated test suite using PyTest framework
* Dockerization of both server and tests
* Create HTML report from test

##### Not implemented
* Including WebSocket support
* Asynchronous server
* performance and WebSocket tests

## Requirements
* Docker (server and test suite were developed on Windows with use of Docker for windows)
* Every additional python modules needed to run code are present in [requirements.txt](requirements.txt) file. Those are installed automatically inside docker containers and do not need to be installed in normal use.

## How to run
##### Automated run
* To build both server and tests Docker images, run **build.bat** file. 
* To run both images and perform full suite of tests run **run.bat** file.
* Tests are performed automatically after running tests container. 
* **reports** catalog will be created on C drive and HTML test report will be stored there after tests container end.

##### Manual run
* To build server image use command:
**docker build -t server -f ./server/Dockerfile .**
* To build tests image use command:
**docker build -t tests -f ./tests/Dockerfile .**

* To create network between Docker containers use command:
**docker network create -d bridge server-tests**
* To run server container use command:
**docker run --network=server-tests --name=server -d server**
* To run tests container use command:
**docker run -v C:\reports\:/usr/src/app/tests/reports --network=server-tests --name=tests -d tests**
* Both containers will run inside "server-tests" network.
* reports" catalog will be created on C drive and HTML test report will be stored there after tests container end.*


### Swagger link
[swagger](openapi3_0.yaml)