FROM python:3.8
ENV PYTHONUNBUFFERED 1 

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry export --without-hashes -f requirements.txt  | pip install -r /dev/stdin

COPY . /app/

