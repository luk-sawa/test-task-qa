FROM python:3.8-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock deploy.sh ./
COPY . ./server

RUN pipenv install --system --deploy

EXPOSE 8080
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]