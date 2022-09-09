# syntax=docker/dockerfile:1
FROM python:3

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ask_others_root /app

WORKDIR /app
