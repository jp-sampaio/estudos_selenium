'''
    Tirando o print da tela, com apenas um comando, pode ser adaptada para diferentes cenários, combinando com outros comandos
'''

from codigo_padrao import iniciar_driver, By
from time import sleep

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
sleep(2)
driver.save_screenshot('tela.jpg')
sleep(1)

input('Print tirado da tela.')
driver.close()