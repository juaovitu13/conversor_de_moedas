import xmltodict

with open("moedas.xml", "rb") as arquivo_moedas:
    dic_moedas = xmltodict.parse(arquivo_moedas)

moedas = dic_moedas["xml"]


with open("conversoes.xml", "rb") as arquivo_conversoes:
        dic_conversoes = xmltodict.parse(arquivo_conversoes)

conversoes = dic_conversoes["xml"]