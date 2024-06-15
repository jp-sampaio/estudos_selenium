'''
    Interagindo com diferentes alertas que aparecem na tela 
'''

from codigo_padrao import iniciar_driver, By
from time import sleep

driver = iniciar_driver()

driver.get('https://cursoautomacao.netlify.app/')
sleep(3)
driver.execute_script('window.scrollTo(0, 950);')
sleep(1)
# Primeiro caso de alerta, onde coloco o meu nome, depois clico em alerta e logo em seguida em ok no alerta
name_field = driver.find_element(By.ID, 'nome')
sleep(1)
name_field.send_keys('João Paulo Sampaio')
sleep(1)
alert_button = driver.find_element(By.ID, 'buttonalerta')
sleep(1)
alert_button.click()
sleep(2)
# Interagindo com o alerta que aparece na tela
alert_one = driver.switch_to.alert
sleep(2)
# Aceitar o botão de confirmação
alert_one.accept()
sleep(3)

# Segundo caso clico no botão de confirmar, e escolho se desejo confirmar ou não
confirm = driver.find_element(By.ID, 'buttonconfirmar')
sleep(1)
confirm.click()
sleep(2)
alert_two = driver.switch_to.alert
sleep(1)
# Não aceita, ou seja não confirma
alert_two.dismiss()
sleep(3) 

# Terceiro caso clico em fazer pergunta, digito alguma coisa no prompt e confirmo ou não e depois em ok
ask_question = driver.find_element(By.ID, 'botaoPrompt')
sleep(2)
ask_question.click()
sleep(1)
alert_three = driver.switch_to.alert
sleep(1)
alert_three.send_keys('15 de junho de 2024')
sleep(2)
alert_three.accept()
sleep(1)
alert_three.accept()

driver.close()
