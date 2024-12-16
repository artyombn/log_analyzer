FROM python:3.12.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip "poetry==1.8.2"

RUN poetry config virtualenvs.create false --local

RUN poetry install --no-dev

RUN apt-get update && apt-get install -y make

COPY . /app

COPY Makefile /app/