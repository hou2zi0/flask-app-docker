from app import app
from flask import request
import json

import spacy 
nlp = spacy.load('en_core_web_sm')


@app.route('/')
def index():
    return "Hello from Flask! 🐵"

@app.route('/api', methods=['GET'])
def api():
    return "Hello from API!"

@app.route('/api/adj', methods=['GET', 'POST'])
def adj():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'text/plain':
            return "Text Message: " + request.data
        elif request.headers['Content-Type'] == 'application/json':
            req = request.json
            if 'text' in req.keys():
                doc = nlp(req['text'])
                res = [ { 'orth': t.orth_, "lemma": t.lemma_} for t in doc if t.pos_ == 'ADJ']
                return f"{json.dumps(res)}"
            else:
                res = 'No key text in request.'
                return res
    else:
        return 'Api error!'