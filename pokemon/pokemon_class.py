class Pokemon(object):
  def __init__(self, response):
    self.weight = response['weight']
    self.name = response['name']
    self.image_url = response['sprites']['front_default']

  def __str__(self):
    return self.name + ', ' + str(self.weight) + ', ' + self.image_url

  def name_len(self):
    return 'This pokemon\'s name has ' + str(len(self.name)) + ' characters.'

  def weight_halved(self):
    return self.weight / 2.0
