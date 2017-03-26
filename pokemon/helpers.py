import random

def build_data(response):
  data = {}

  data['name'] = response['name']
  data['weight'] = response['weight']
  data['image_url'] = response['sprites']['front_default']

  return data

def set_url():
  num = random.randint(1, 25)
  return 'http://pokeapi.co/api/v2/pokemon/' + str(num)