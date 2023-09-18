# Dockerfile

# pull the official docker image
FROM python:3.7-alpine

# set work directory
#WORKDIR /app/
#ADD . /app/

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .