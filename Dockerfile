FROM debian

RUN apt-get update
RUN apt-get install python2.7 python-pip -y
RUN mkdir app
RUN pip install gunicorn
RUN pip install flask
ADD app.py /app/
WORKDIR /app/
CMD ["gunicorn","-b", "127.0.0.1:8000", "app:app"]
