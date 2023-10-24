import os
import time
#criar navegador 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#interagir com elementos


#https://www.elcorteingles.pt/supermercado/
#https://www.garrafeirasoares.pt/pt/
#
html = "https://www.continente.pt/"
navegador.get(html)

try:
    #tratamento cooki continet
    cookie_button = navegador.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    #tratamento cooki continet
    button = navegador.find_element(By.CSS_SELECTOR, 'button[aria-label="Introduza o termo que deseja pesquisar"]').click()
    search_input = navegador.find_element(By.CSS_SELECTOR, 'input[aria-label="Introduza o termo que deseja pesquisar"]').send_keys("5601012001310")





except Exception as e:
    print(f"Ocorreu um erro: {e}")

    # Click on the search icon\


    
    
    
    
     
    
    # Insira algum texto na caixa de pesquisa
   


input("Pressione Enter para fechar o navegador...")
navegador.quit()


