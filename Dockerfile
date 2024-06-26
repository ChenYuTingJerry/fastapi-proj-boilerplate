ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-alpine as builder

# prepare poetry env
ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN apk add --no-cache \
    build-base \
    libffi-dev

RUN --mount=type=cache,target=$POETRY_CACHE_DIR pip install poetry

# install dependencies
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

# run app
FROM python:${PYTHON_VERSION}-alpine as runtime
ENV VIRTUAL_ENV=/app/.venv \
    PATH=/app/.venv/bin:$PATH
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV
WORKDIR /app
COPY app ./

ENTRYPOINT ["gunicorn"]
CMD ["main:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0"]
