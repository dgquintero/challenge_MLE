# syntax=docker/dockerfile:1.2
FROM python:latest
# put you docker configuration here

WORKDIR /challenge

COPY . .

RUN pip install -r requirements-dev.txt

CMD ["uvicorn", "challenge.api:app", "--host", "0.0.0.0", "--port", "80"]
