FROM python:3.8-slim

RUN apt-get -y update && apt-get -y upgrade && apt-get -y clean
RUN mkdir /app 
RUN useradd -m user && chown -R user:user /app
USER user:user
RUN pip install flask Flask-Mail
COPY app.py /app
WORKDIR /app
ENTRYPOINT "python3"
