FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk add --update --virtual .builddeps python3-dev libffi-dev openssl-dev build-base && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del .builddeps

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]