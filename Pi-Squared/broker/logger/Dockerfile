FROM python:3.9

# RUN useradd -ms /bin/bash lg
# USER lg

WORKDIR /lg/
ADD start.sh .
#ENV FLASK_APP=logger.py 

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


CMD ["./start.sh"]