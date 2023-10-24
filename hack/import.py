
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


# Defina um valor de tempo limite (timeout) em segundos
timeout = 30

# Crie opções para o driver
options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Isso torna o navegador invisível

# Inicialize o driver usando o valor de tempo limite definido
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options, service_args=["--connect-timeout=" + str(timeout)])

#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://www.continente.pt/pesquisa/?q=")

# Localize os elementos que contêm informações de produtos (substitua pelo seletor CSS apropriado)
product_elements = driver.find_elements_by_css_selector('.product')

# Crie uma lista para armazenar os códigos EAN
ean_list = [5601012011302, 5601012011920, 5601012011920 ]

# Itere pelos elementos e colete os códigos EAN
for product_element in product_elements:
    ean_element = product_element.find_element_by_css_selector('ean')
    ean = ean_element.text
    ean_list.append(ean)

# Imprima os códigos EAN coletados
for ean in ean_list:
    print("EAN:", ean)

# Feche o navegador
driver.quit()