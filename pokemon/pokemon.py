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
  url = set_url()

  r = requests.get(url)

  r_json = json.loads(r.text)
  data = build_data(r_json)

  return json.dumps(data)