FROM python:3.8-alpine

WORKDIR /home/app

COPY  project/requirements.txt .

RUN apk update \
    && apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --virtual build-deps \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk del build-deps

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt
RUN pip3 install gunicorn
