FROM python:3.8-slim-buster
RUN pip3 install --upgrade pip

WORKDIR /app
COPY . /app

#RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get --assume-yes install gcc
RUN pip3 install cython
RUN pip3 install uwsgi
RUN pip3 install -r requirements.txt
RUN	python3 -m spacy download en_core_web_sm


#ENTRYPOINT ["python3"]
#CMD ["run.py"]

CMD [ "uwsgi", "app.ini" ]