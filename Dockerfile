FROM python:3.8

COPY . /root

WORKDIR /root

RUN pip install flask gunicorn