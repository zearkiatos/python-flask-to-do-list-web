FROM python:alpine3.17

COPY . /app/

WORKDIR /app

RUN apk add g++ jpeg-dev zlib-dev libjpeg make
RUN apk add libffi-dev
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["main.py" ]