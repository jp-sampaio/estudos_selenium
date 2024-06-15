'''
    Para fechar uma aba eu posso utilizar o mesmo processo de fechar uma janela e adquirir o seu endereço para transitar entre elas
'''

from codigo_padrao import iniciar_driver, By
from time import sleep
from random import randint

driver = iniciar_driver()

def write_smoothly(text, element):
    for row in text:
        element.send_keys(row)
        sleep(randint(1, 10) / 30)

senha = '1245minhasenha'

driver.get('https://cursoautomacao.netlify.app/')
sleep(3)
home_page = driver.current_window_handle
driver.execute_script('window.scrollTo(0, 900);')
sleep(2)
open_tab_button = driver.find_element(By.XPATH, '//button[text()="Abrir aba"]')
sleep(1)
driver.execute_script('arguments[0].click()', open_tab_button)
sleep(3)
windows = driver.window_handles
for window in windows:
    if window not in home_page:
        driver.switch_to.window(window)
        password_field = driver.find_element(By.ID, 'senha')
        sleep(2)
        write_smoothly(senha, password_field)
        sleep(2)
        driver.close()

driver.switch_to.window(home_page)

driver.close()
input('Finalizado!!!')
