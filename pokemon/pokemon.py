import os

# import Flask class
from flask import Flask, render_template

# import all functions from helpers
from helpers import *

# import libraries
import requests
import json

# instance of Flask
app = Flask(__name__)

@app.route('/')
def index():
  url = set_url()
  response = requests.get(url)

  r_json = json.loads(response.text)
  data = build_data(r_json)

  return render_template('pokemon.html', pokemon=data)