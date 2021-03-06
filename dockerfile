FROM python:3.8-slim-buster

WORKDIR /hello

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=src.server
ENV FLASK_ENV=development
EXPOSE 5000
CMD ["python3", "-m" , "flask", "run", "--host", "0.0.0.0"]
