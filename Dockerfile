FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1 


WORKDIR /app
#required for daphne (when using python slim)
RUN apt-get update && apt install -y --no-install-recommends build-essential

RUN pip install poetry
COPY pyproject.toml poetry.lock /app/

RUN poetry export --without-hashes -f requirements.txt  | pip install -r /dev/stdin

COPY . /app
#Make executable
RUN chmod u=rx ./wait-for-it.sh
RUN echo "I am $(whoami)"
#RUN ["chmod","u=rx", "./wait-for-it.sh"]
