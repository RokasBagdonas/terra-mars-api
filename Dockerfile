FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1 

WORKDIR /app
#required for daphne (when using python slim)
RUN apt-get update && apt install -y --no-install-recommends build-essential

RUN pip install poetry
COPY pyproject.toml poetry.lock /app/

#primarily used for installing pytest
ARG POETRY_EXPORT_FLAGS
RUN poetry export ${POETRY_EXPORT_FLAGS} --without-hashes -f requirements.txt  | pip install -r /dev/stdin

COPY . /app
