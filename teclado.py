'''
    Para utilizar as teclas do meu teclado, eu tenho que importar a biblioteca do selenium Keys
'''

from codigo_padrao import iniciar_driver, By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = iniciar_driver()

driver.get('https://cursoautomacao.netlify.app/')
sleep(1)

dropdown = driver.find_element(By.ID, 'paisselect')
sleep(2)
dropdown.click()
sleep(1)
for x in range(2):
    dropdown.send_keys(Keys.ARROW_DOWN)
    sleep(1.5)


input('Finalizado!!!')
driver.close()