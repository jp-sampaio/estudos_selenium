'''
    A maneira de trabalhar com iframe, preciso entrar dentro dele, muito parecido com o que acontece em uma página window
'''

from codigo_padrao import iniciar_driver, By
from time import sleep

driver = iniciar_driver()

driver.get('https://cursoautomacao.netlify.app/')
sleep(3)
# Rolar a página até o seu final
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(2)
# Entrar dentro do iframe
iframe = driver.find_element(By.XPATH, '//iframe[@src="https://cursoautomacao.netlify.app/desafios.html"]')
# Trocando o foco agora para dentro do iframe
driver.switch_to.frame(iframe)
sleep(2)
name_field = driver.find_element(By.ID, 'dadosusuario')
sleep(1)
name_field.send_keys('João Paulo Sampaio')
sleep(2)
click_here_button = driver.find_element(By.ID, 'desafio2')
sleep(1)
click_here_button.click()
sleep(2)
# Sair do iframe e voltar para a página padrão
driver.switch_to.default_content()

driver.close()