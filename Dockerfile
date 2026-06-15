FROM python:3.14-alpine

ENV PYTHONUNBUFFERED=1

ADD . /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000/tcp
