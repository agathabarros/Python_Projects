import os
import time
#criar navegador 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#interagir com elementos



html = "https://www.continente.pt/"
navegador.get(html)

try:
    #tratamento cookie
    element = navegador.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
except Exception as e:
    print(f"Ocorreu um erro: {e}")

    list_elements = navegador.find_elements(By.XPATH, '//*[@id="brand-header"]/nav/div/div[1]')
    for elements in list_elements:
        if "search" in list_elements.text.lower():
            elements.click()
            break

    
    
     
    
    # Insira algum texto na caixa de pesquisa
   


input("Pressione Enter para fechar o navegador...")
navegador.quit()


