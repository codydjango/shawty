FROM python:3.6-alpine

RUN apk update && apk upgrade
RUN apk add git bash build-base gcc python3-dev musl-dev postgresql-dev
RUN pip install --upgrade pip
RUN pip install psycopg2 flask flask-sqlalchemy graphene Flask-GraphQL

COPY ./src /app/src
SHELL ["/bin/bash", "-c"]

ENV APP_HOST=0.0.0.0
ENV APP_PORT=3001
ENV FLASK_APP=/app/src/app.py
ENV FLASK_ENV=development

ENTRYPOINT flask run --host=${APP_HOST} --port=${APP_PORT}
