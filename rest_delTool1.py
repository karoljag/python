from time import sleep
import requests
import json
import urllib
headers = {'content-type': 'application/json'}
raw = urllib.urlopen('http://orange-dev.isaacloud.com/api/users?limit=10000')
json_object = json.load(raw)
for i in range (0,100):
	us = json_object[i]["id"]
	dele  = requests.delete('http://orange-dev.isaacloud.com/api/users/'+us)
	sleep(0.1)
	print us
	