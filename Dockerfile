FROM python:3.6

WORKDIR .
COPY requirements.txt requirements.txt
COPY . /app
RUN pip install -r requirements.txt