FROM python:latest

WORKDIR /logging-client/

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY logging_client.py .

CMD ["python3", "./logging_client.py"]