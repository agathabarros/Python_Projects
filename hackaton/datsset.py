import sqlite3
import requests

url = "https://www.continente.pt/pesquisa/"
response = requests.get(url)

if response.status_code == 200:
    html = response.text
else:
    print("Falha na solicitação HTTP.")

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

# Exemplo: Extrair texto de um elemento com a classe "exemplo"
elemento = soup.find("ean", class_="&ean=560")
dado = elemento.csv


conn = sqlite3.connect(dado)

cursor = conn.cursor()

# Exemplo: Criação de uma tabela de produtos com colunas de ID, nome e preço
cursor.execute('''
    CREATE TABLE produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL
    )
''')

# Salve as alterações no banco de dados
conn.commit()


""" 
from eansearch import EANSearch

apiToken = "abcdef"

eansearch = EANSearch(apiToken)
eanList = eansearch.barcodePrefixSearch('560');
for product in eanList:
	print(product["ean"], " is ", product["name"].encode("utf-8")) """