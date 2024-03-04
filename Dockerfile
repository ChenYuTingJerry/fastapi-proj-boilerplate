FROM python:3.11-alpine as builder

# prepare potry env
ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# install your app
COPY pyproject.toml poetry.lock ./

WORKDIR /app
