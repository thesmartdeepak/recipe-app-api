FROM python:3.9-alpine3.13
LABEL maintainer="Deepak Kumar"

ENV PYTHONBUFFERED 1

COPY requirements.txt /tmp/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt
COPY . ./app

RUN ls

WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN apk add --upgrade --no-cache postgresql-client
RUN apk add --upgrade --no-cache --virtual .tmp-build-deps build-base postgresql-dev musl-dev
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN pip install -r /tmp/requirements.dev.txt
RUN apk del .tmp-build-deps

ENV PATH="/py/bin:$PATH"