from time import sleep
import requests
import json
import urllib
headers = {'content-type': 'application/json'}
raw = urllib.urlopen('http://orange-dev.isaacloud.com/api/users?limit=10000')
json_object = json.load(raw)

lolko = '{"id":"lolko","tags":["importer","jetblue"],"groups":[],"status":"enabled","lastLogin":null,"updatedAt":"2016-06-16T14:15:47+01:00","isAdmin":false,"history":[],"email":null,"isMerged":null,"lastName":"Nazwisko","firstName":"Imie","points":0,"birthDate":null,"enrollmentDate":null,"createdAt":"2016-06-16T14:15:47+01:00","isActive":true,"avatars":[],"socials":{"facebookId":null,"twitterId":null,"appInvites":{"facebook":[]},"facebookFriendsIds":[]},"gender":null,"level":1}'

for i in range (0,1000):
	us0 = json_object[i]["id"]
	us1 = json_object[i+1]["id"]
	get0  = requests.get('http://orange-dev.isaacloud.com/api/users/'+us0)
	# get1  = requests.get('http://orange-dev.isaacloud.com/api/users/'+us1)
	# sleep(0.01)
	# print get0.text
	# print get1.text
	if i == 100:
		print i
	
	if lolko == get0:
		print "ROWNE"
    







	
 