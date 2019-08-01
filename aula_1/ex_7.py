import requests


URL = 'https://gen-net.herokuapp.com/api/users/{}'


payload = {
	'nome': input('Digite seu nome: '), 
	'email': input('digite seu email: '),
	'password': input('digite seu senha: ')

		}
response = requests.post(URL, payload)

if response.status_code == 200:
	user_id = response.json().get('id')
	print = ('usuario {} cadastrado com sucesso'.format(user_id) 
		)
else:
		print = ('Email já cadastrado')