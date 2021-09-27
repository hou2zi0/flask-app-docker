FROM alpine:latest
RUN apk add --no-cache python3-dev 
RUN apk add --no-cache py3-pip

WORKDIR /app
COPY . /app

#RUN pip3 install -r requirements.txt

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; 
	
RUN	pip3 install -r requirements.txt; \
	apk del .build-deps;

#ENTRYPOINT ["python3"]
#CMD ["run.py"]

CMD [ "uwsgi", "app.ini" ]
