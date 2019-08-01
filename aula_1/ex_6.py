import requests 

URL = 'https://gen-net.herokuapp.com/api/users/{}'


user_id = input('digite seu id: ')

response = requests.get(URL.format(user_id))

if response.status_code == 200:
	print(response.json().get('name'))
else: 
	print(response.text)