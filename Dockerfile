FROM python:3.9-slim-buster
USER root

WORKDIR /python-flask

COPY requirements.txt  requirements.txt

RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]