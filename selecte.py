'''
    Trabalhando com o select e pegando os seus elementos de diferentes maneiras
'''

from codigo_padrao import iniciar_driver, By
from selenium.webdriver.support.select import Select
from time import sleep

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
sleep(2)

select_paises = driver.find_element(By.XPATH, '//select[@id="paisselect"]')
opcoes_paises = Select(select_paises)
sleep(1)

# Pegar o elemento por indice
opcoes_paises.select_by_index(2)
sleep(1)

# Pegar o elemento por value
opcoes_paises.select_by_value('estadosunidos')
sleep(1)

# Pegar o elemento por texto exibido 
opcoes_paises.select_by_visible_text('Brasil')
sleep(1)

# Desafio 
desafio = driver.find_element(By.LINK_TEXT, 'Desafios')
sleep(1)
desafio.click()
sleep(1)
driver.execute_script('window.scrollTo(0, 2300);')
sleep(1)
paises_select = driver.find_element(By.XPATH, '//select[@id="paisesselect"]')
selecionar_pais = Select(paises_select)
sleep(1)
selecionar_pais.select_by_index(2)
sleep(1)
selecionar_pais.select_by_value('africa')
sleep(1)
selecionar_pais.select_by_visible_text('Chille')


input('Automação concluída!')
driver.close()
