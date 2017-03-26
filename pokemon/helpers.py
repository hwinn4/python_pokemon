def build_data(response):
  data = {}

  data['name'] = response['name']
  data['weight'] = response['weight']
  data['image_url'] = response['sprites']['front_default']

  return data
