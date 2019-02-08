
from os import environ
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://{0}:{1}@{2}'.format(environ['MONGO_USER'], environ['MONGO_PASS'], environ['MONGO_HOST']))
db = client['512']

@app.route('/')
def index():
  
  if not db.usuarios.find_one():
    for i, u in enumerate(['Hector', 'Jefferson', 'Jaime', 'Ricardo Gonçalves', 'Ricardo Poloni', 'Mauricio', 'Hamilton', 'João', 'Diego Felipe Mateus']):
      db.usuarios.insert({'_id' : i, 'nome' : u})
  
  return jsonify([u for u in db.usuarios.find()])

app.run(host='0.0.0.0')
