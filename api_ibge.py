import requests, json

nome = input("Qual seu nome? ")
resultado = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/Luciano" + nome)

json_dados = json.loads(resultado.text)

print(json_dados[0]['res'][0])

