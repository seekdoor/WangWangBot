FROM python:latest

RUN apt-get update && apt upgrade -y
RUN cd /
COPY . /WangWangBot/
RUN cd WangWangBot
WORKDIR /WangWangBot
RUN apt-get install -y docker-compose
RUN pip3 install -U -r requirements.txt
WORKDIR /data
CMD python3 /WangWangBot/main.py