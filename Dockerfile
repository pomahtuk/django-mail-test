FROM python:3-slim

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 80
CMD ["./run.sh"]