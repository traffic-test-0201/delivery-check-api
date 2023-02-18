FROM python:3.9-slim-buster

COPY . /app

RUN pip3 install flask pymysql

WORKDIR /app



CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
