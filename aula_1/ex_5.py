import requests 

URL = 'https://gen-net.herokuapp.com/api/users/{}'


user_id = input('digite seu id: ')
name = input('digite seu nome: ')
email = input('digite seu email: ')
password = input('digite sua senha: ')


payload = {
	'nome': nome,
	'email': email,
	'password': password
}

response = requests.get(URL.format(user_id), payload)

if response.status code == 200:
print('Usuario atualizado com sucesso')
else 
print('erro ao atualizar o usuario')