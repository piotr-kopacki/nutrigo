FROM python:3

COPY ./ ./

RUN pip install -r requirements.txt

# Problematic line
RUN python -m textblob.download_corpora

CMD [ "python", "manage.py", "runserver"]
