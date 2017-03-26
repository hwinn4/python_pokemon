import pytest
from pokemon.helpers import *

class TestHelpers():
  def test_build_data(self):
    result = {"image_url": "https://pokemon/8.png", "name": "wartortle", "weight": 225}
    sample_response = {
                        "blah": "blah",
                        "name": "wartortle", "weight": 225,
                        "sprites" : { "front_default" : "https://pokemon/8.png" }
                      }

    assert build_data(sample_response) == result

  def test_set_url(self):
    nums = range(0, 75)
    result = set_url()
    num_arg = int(result.split('/')[-1])
    assert num_arg in nums