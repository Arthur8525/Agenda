import requests

response = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/arthur')
print(response.json())

data = response.json() 

for item in data[0]['res']:
    print(f"Período: {item['periodo']}, Frequência: {item['frequencia']}")
