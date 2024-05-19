docker network create -d bridge server-tests
docker run --network=server-tests --name=server -d server
docker run -v C:\reports\:/usr/src/app/tests/reports --network=server-tests --name=tests -d tests