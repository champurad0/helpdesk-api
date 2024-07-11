FROM python:3.9-alpine3.13 
LABEL maintainer="ginoduarte.com"

ENV PYTHONUNBUFFERED 1

COPY ./app /app 
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt 
WORKDIR /app 
EXPOSE 8000 

ARG DEV=false
RUN python -m venv /py && \ 
  /py/bin/pip install --upgrade pip && \
  /py/bin/pip install -r /tmp/requirements.txt && \
  if [ $DEV ="true" ]; \
  then /py/bin/pip install -r requirements.dev.txt ; \
  fi && \ 
  rm -rf /tmp && \
  adduser \
  --disabled-password \
  --no-create-home \
  django-user

ENV PATH="/pv/bin:$PATH"

USER django-user 
