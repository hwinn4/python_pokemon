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