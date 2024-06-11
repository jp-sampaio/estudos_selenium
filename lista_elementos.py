'''
    Clicar em uma lista de elementos seja de forma individual e de maneira agrupada
'''

from codigo_padrao import iniciar_driver, By
from time import sleep
from random import randint

# Inicializar o driver para entrar no navegador
driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
sleep(2)
driver.maximize_window()
sleep(1)
desafios = driver.find_element(By.LINK_TEXT, 'Desafios')
sleep(1)
desafios.click()
sleep(1)
driver.execute_script('window.scrollTo(0, 1300);')
sleep(1)
checkboxs_carros = driver.find_elements(By.NAME, 'carros')
sleep(1)
checkboxs_carros[1].click()
sleep(1)
checkboxs_carros[3].click()
sleep(1)
checkboxs_carros[4].click()
sleep(1)
driver.execute_script('window.scrollTo(0, 1500);')
sleep(3)
checkboxs_motos = driver.find_elements(By.NAME, 'motos')
sleep(1)
for moto in checkboxs_motos:
    moto.click()
    sleep(randint(1,5) / 20)


input('Automação concluída com sucesso!')
driver.close()
