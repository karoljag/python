# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import requests
# import json
# import urllib2

# resp = requests.get('http://qbo-dev.isaacloud.com/users')
# if resp.status_code != 200:
# 	print "pppp"

# # payload = {"name": "usPy"}
# # r = requests.get("http://qbo-dev.isaacloud.com/users")
# # print(r.text)



# data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
# data = json.dumps(data)

# # # re = r.text
# # # print re
# # print r.json()
# # r = requests.post('http://qbo-dev.isaacloud.com/users', headers={'Content-Type': 'application/json'},data = {"name": "usPy2"})
# # print r.status_code 


# # gh_url = 'https://api.github.com'

# # req = urllib2.Request(gh_url)

# # print req

from time import sleep


import requests
import json
import urllib
headers = {'content-type': 'application/json'}


# data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
# # params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

# data2 = {
#     # 
#     "name":"name",
#     "tags": [],
#     "groups": [],
#     "defaultKey": "defaultValue",
#     "nameKey": "nameValue"
#   }
# # for e in range (0,500):
# 	requests.post(url, data=json.dumps(data2), headers=headers)

# 	response = requests.post(url, data=json.dumps(data2), headers=headers)
# 	# print response.status_code

# 	# print response.text
# 	# print response.content
# 	tr = response.content
# 	# print tr

# 	dat =  response.json()
# 	print dat["id"]
# 	sleep(0.1)
# pod = tr.split(',')

# print pod
# data3 = {
#     #
#     # "id":"30mar",
#     "name":"30mar",
#     "tags": [],
#     "groups": [],
#     "defaultKey": "defaultValue",
#     "nameKey": "nameValue"
#   }

# url1 = 'http://qbo-dev.isaacloud.com/users/30mar'
# r = requests.put(url1, data=json.dumps(data3), headers=headers)
# print r.json()
# ee = r.json()

# resp = requests.get('http://qbo-dev.isaacloud.com/users?limit=10000')
# if resp.status_code != 200:
# 	print "pppp"


# we = resp.json()
# print len(we)


raw = urllib.urlopen('http://orange-dev.isaacloud.com/api/users?limit=10000')
# json_raw = raw.readlines()
json_object = json.load(raw)
# print json_object
# print json_object[0]["id"]

# print len (json_object)

for i in range (0,100):
	# print json_object[i]["id"]
	us = json_object[i]["id"]
	# dele  = requests.delete('http://orange-dev.isaacloud.com/api/users/'+us)
	sleep(0.05)
	print us
	# print dele.status_code