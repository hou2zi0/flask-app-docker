FROM alpine:latest
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["run.py"]