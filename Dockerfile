FROM python:3

COPY ./src/requirements.txt ./app/

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 80

CMD [ "python3", "-u", "/app/src/main.py" ]

