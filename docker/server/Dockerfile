FROM python

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirement_server.txt .
RUN pip install -r requirement_server.txt

COPY . /usr/src/app/

