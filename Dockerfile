FROM python:3.6-alpine

MAINTAINER Rutger Drubbel

RUN python3.6 -m pip install --upgrade pip

COPY . /app

WORKDIR /app

#RUN pip install requests
#RUN pip install flask
RUN pip install -r requirements.txt

CMD ["python3.6", "app.py"]
