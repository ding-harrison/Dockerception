FROM python:3.6.9-alpine

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apk add docker

COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]
