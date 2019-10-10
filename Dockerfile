FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install pipenv
RUN pipenv install --sequential --deploy --ignore-pipfile --dev
RUN pipenv run python -m textblob.download_corpora

