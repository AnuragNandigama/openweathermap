FROM python:3.10.2-alpine3.15

ADD . /openweathermap

WORKDIR /openweathermap

RUN pip install -r requirements.txt

CMD ["python", "app.py"]