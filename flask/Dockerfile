FROM alpine:latest
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

WORKDIR /app
COPY . /app

#RUN pip3 install -r requirements.txt

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip3 install -r requirements.txt; \
	apk del .build-deps;

#ENTRYPOINT ["python3"]
#CMD ["run.py"]

CMD [ "uwsgi", "app.ini" ]