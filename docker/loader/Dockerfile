FROM python

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirement_loader.txt .
RUN pip install -r requirement_loader.txt

COPY . /usr/src/app/

