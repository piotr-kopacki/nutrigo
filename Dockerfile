FROM python:3

EXPOSE 8000

COPY ./ ./

RUN pip install -r requirements.txt

# Problematic line
RUN python -m textblob.download_corpora

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
