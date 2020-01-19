# Flask & Docker

## Hilfreiche Befehle

### Docker
* Hilfe erhalten: `docker --help`

#### Erstellung
* Container erstellen: `docker build -t image-name:tag .`
* Mehrere Container auf einmal erstellen und hochfahren: `docker-compose up --build`

#### Starten & Stoppen von Cotainern
* Container mit Port-Mapping Host:Guest starten: `docker run -d -p 80:5000 image-name`; die Option `-p` mappt einen Port in den Container.
* Container mit Portm-Mapping Host:Guest und gesetzter Environment-Variable (für WSGI) starten: `docker run -d -p 80:5000 -e PORT=5000 image-name`; `-e PORT=5000` belegt die Variable `PORT` in der uWSGI-ini-Datei (`app.ini`) mit dem übergeben Wert, e.g. `5000`, der mit dem Host:Guest Port-Mapping korrespondiert. 
* Container hochfahren: `docker start Container_ID`
* Container herunterfahren: `docker stop Container_ID`

#### Überblick behalten
* Alle images auflisten: `docker images -a`
* Alle Container auflisten: `docker ps -a`

#### Löschen
* Einen oder mehrere Container löschen: `docker rm Container_IDs` 
* Ein oder mehrere Images löschen: `docker rmi Image_IDs`

### Heroku
* Allgemeine Hilfe: `heroku --help`
* Hilfe zum Container-Deployment: `heroku container --help`

#### Container-Deployment
* `heroku create AppName`  Erstellt eine neue App innerhalb deines Heroku-Accounts.
* `heroku container:push web -a AppName` Erstellt eine neue App auf Basis einer `Dockerfile`-Datei und lädt die App in deinen Account hoch.
* `heroku container:release web -a AppName` Schaltet die mit `container:push` erstellte App online frei, so dass sie für jeden im Web erreichbar ist.
* `heroku logs -a AppName` Gibt die Log-Dateien der App aus. Sehr wichtig, um bspw. Konfigurationsfehler des Web Server Gateway Interfaces (WSGI) zu aufzuspüren.
* `heroku open -a AppName` Öffnet die App im Web-Browser.

#### Apps
* Alle Apps auflisten: `heroku apps`
* Information zu einzelner App: `heroku apps:info AppName`

## Requests

* JSON: `curl -d '{"text":"I am a pretty monkey!"}' -H "Content-Type: application/json" -X POST http://127.0.0.1/api/adj`

## Troubleshooting

* Start Python with the envs python version: `python -m flask run`, when you encounter problems while loading the libs within the running flask instance.

## Tutorials
* [Containerise your Python Flask using Docker and deploy it on Heroku](https://medium.com/@ksashok/containerise-your-python-flask-using-docker-and-deploy-it-onto-heroku-a0b48d025e43)
* [Containerizing Python web apps with Docker, Flask, Nginx & uWSGI](https://www.youtube.com/watch?v=dVEjSmKFUVI)
