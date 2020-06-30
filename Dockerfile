FROM python:3.8

ADD . /app

RUN pip install -r ./app/requirements.txt

WORKDIR /app

CMD ["python", "manage.py","runserver"]

EXPOSE 8000
