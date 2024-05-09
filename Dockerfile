FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]