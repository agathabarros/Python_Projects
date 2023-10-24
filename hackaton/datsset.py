import sqlite3

conn = sqlite3.connect('sogrape_analytics.csv')

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
eanList = eansearch.barcodePrefixSearch('0885909');
for product in eanList:
	print(product["ean"], " is ", product["name"].encode("utf-8")) """