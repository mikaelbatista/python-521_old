import requests 

URL = 	'https://gen-net.herokuapp.com/api/users/'

response = requests.get(URL)

print(res.status_code)

users = response.json()

email = input('digite seu email: ')

chaves = [ u.keys() for u in users ]
chaves = sorted ( 
for user in users:
if user.get('email') == email:
print(user)
