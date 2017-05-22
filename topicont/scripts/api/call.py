import requests
import json

url = "https://api.telegram.org/bot349241397:AAEWAb5C70yUhFNDt8t8JOTNUK4xCKBt8To/"

def get_me():
	response = requests.get(url + 'getMe')
	return response.json()

def get_updates_json():
	response = requests.get(url + 'getUpdates')
	return response.json()

def last_update(data):
	results = data['result']
	total_updates = len(results) - 1
	return results[total_updates]
