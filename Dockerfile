# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /weather

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "2", "main:app", "-b", "0.0.0.0:8080"]
