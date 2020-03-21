import base64, requests, lxml, json

host = 'https://wa.boteater.us/api'
headers = {
	'apikey': 'API KEY SENDIRI',
	'userid': 'USER ID SENDIRI',
	'username': 'USERNAME SENDIRI'
}

url = host + '/client'
a = requests.get(url, headers=headers)
print(a.text)