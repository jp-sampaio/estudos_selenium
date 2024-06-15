'''
    Utilizando o actions chains para usar o botão direito do mouse e também o teclado e fazer movimentos dentro da página, posso utilizar várias maneiras diferentes de mover o mouse ou escrever na tela alguma informação que desejo passar para o usuário.
'''

from codigo_padrao import iniciar_driver, By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = iniciar_driver()

driver.get('https://cursoautomacao.netlify.app/exemplo_chains')
sleep(3)
right_button = driver.find_element(By.ID, 'botao-direito')
sleep(2)
chains = ActionChains(driver)
# Clicando com o botão direito nesse campo e depois mover com as teclas para baixo e para cima, clicar e depois confirmar
chains.context_click(right_button).pause(2).send_keys(Keys.DOWN).pause(2).send_keys(Keys.DOWN).pause(3).send_keys(Keys.UP).pause(1).send_keys(Keys.DOWN).pause(3).click().perform()

input('...')
driver.close()
