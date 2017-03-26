# import Flask class
from flask import Flask

# import all functions from helpers
from helpers import *

# import libraries
import requests
import json

# instance of Flask
app = Flask(__name__)

@app.route('/')
def index():
  r = requests.get('http://pokeapi.co/api/v2/pokemon/8')
  r_json = json.loads(r.text)
  data = build_data(r_json)
  return json.dumps(data)