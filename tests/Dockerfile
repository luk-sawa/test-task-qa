FROM python:3.8-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src/app
COPY ../requirements.txt ./
COPY ../run_tests.sh ./
COPY ./tests ./tests

RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["/usr/src/app/run_tests.sh"]