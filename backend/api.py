import requests
import json


def get_recepy_json():
    response = requests.get("http://localhost:8000/api/recept/")
    return json.loads(response.text)

def get_restaurant_json():
    response = requests.get("http://localhost:8000/api/restaurant/")
    return json.loads(response.text)

