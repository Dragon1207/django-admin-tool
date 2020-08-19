FROM python:3.8-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_HIDE_EMOJIS=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true \
  C_FORCE_ROOT=true \
  POETRY_VERSION=1.0.9 \
  PATH="/root/.poetry/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN apt update \
    && apt install -y make \
                      curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/${POETRY_VERSION}/get-poetry.py | python \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root \
    && apt autoremove -y

COPY . .

RUN poetry install --no-interaction --no-ansi -E jaeger
