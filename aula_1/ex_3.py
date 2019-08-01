import requests 

URL =  'https://viacep.com.br/ws/{}/json'

cep = input('digite seu cep: ')

response = requests.get(URL.format(cep)) 

print(response.json())
