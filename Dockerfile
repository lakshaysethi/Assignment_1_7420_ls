FROM python:3-alpine

ADD . /app

RUN pip install -r ./app/requirements.txt

WORKDIR /app

CMD ["python", "manage.py","runserver"]