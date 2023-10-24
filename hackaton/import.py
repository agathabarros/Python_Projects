import selenium
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
navegador = webdriver.Chrome(service=servico)

import os

caminho = os.getcwd()
arquivo = caminho + "https://www.continente.pt/produto/mateus-vinho-rose-mateus-2922551.html"
navegador.get(arquivo)

from selenium.webdriver.common.by import By

titulo = navegador.find_element(By.TAG_NAME, 'h2').text
print(titulo)

numero_whatsapp = navegador.find_element(By.PARTIAL_LINK_TEXT, '&ean=').text
print(numero_whatsapp)

navegador.find_element(By.NAME, 'email').send_keys("pythonimpressionador@gmail.com")