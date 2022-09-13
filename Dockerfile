# syntax=docker/dockerfile:1
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /code
COPY . .

RUN pip install -r requirements.txt
RUN apt-get -q update && apt install wait-for-it

WORKDIR /code/ask_others_root
