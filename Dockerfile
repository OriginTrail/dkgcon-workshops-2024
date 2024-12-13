FROM python:3.11-slim-buster

WORKDIR /workshop

# prevent generation of .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# turn of buffering for easier container logging
ENV PYTHONUNBUFFERED 1

COPY . /workshop/

RUN apt-get update && \
  apt-get install -y vim
# RUN /workshop/install.sh

EXPOSE 8900 9000
