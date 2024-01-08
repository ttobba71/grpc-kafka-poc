FROM python:3.11-bullseye as base

# The base image sets LANG=C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONHASHSEED 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'

FROM base as builder
# install a few utilities
ARG SHELL_UTILS="bash-completion curl less libpq-dev vim netcat-traditional binutils libproj-dev git"
RUN apt-get update && apt-get install -y ${SHELL_UTILS} \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get install -y libcurl4-openssl-dev

#RUN apt-get install -y postgresql-client
#RUN apt-get install -y kafkacat

# Poetry for dependencies
RUN pip install --upgrade pip

RUN mkdir -p /usr/src/app

COPY ./pyproject.toml  /usr/src/app
COPY ./poetry.lock     /usr/src/app

# Install Poetry and related dependencies
ARG POETRY_DEPS="poetry toml"
RUN pip install ${POETRY_DEPS} --no-cache-dir

#ARG BUILD_DEPS=""
#RUN apt-get install -y ${BUILD_DEPS}

RUN --mount=type=cache,target="$POETRY_CACHE_DIR"

RUN poetry config virtualenvs.create false

FROM builder as final

RUN poetry install --no-interaction --no-ansi
WORKDIR /usr/src/app/

COPY . /usr/src/app

RUN mkdir /etc/certs

CMD bin/entrypoint.sh
