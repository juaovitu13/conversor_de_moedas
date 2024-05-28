import requests

link = f"https://economia.awesomeapi.com.br/last/USD-BRL"

requisicao = requests.get(link)

print(requisicao)