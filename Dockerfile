FROM python:3.8

ADD . /app

RUN pip install -r ./app/requirements.txt

WORKDIR /app

ENV AWS_ACCESS_KEY_ID AKIARFOBAEDYRRQHGTAU
ENV AWS_SECRET_ACCESS_KEY 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
ENV REDIS_URL redis://h:p6fdceaa6cb334d32165b6f8a7c960a13d844cb54518f879af85ecbf10debd990@ec2-18-232-246-26.compute-1.amazonaws.com:21329
ENV SENDGRID_API_KEY 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
ENV DATABASE_URL postgres://tvejastaqjnrik:8054853d2a281930d86495649afbf3dcead456072b6ee4d4cccf371112754ae3@ec2-3-216-129-140.compute-1.amazonaws.com:5432/d6g38qj54uqh4n
CMD ["python", "manage.py","runserver","0.0.0.0:8000"]

EXPOSE 8000
