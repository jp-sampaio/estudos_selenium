'''
    Entendendo o funcionamento do checkbox e como clicar e saber se ele está selecionado
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,700', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')

# checkboxs = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
# sleep(3)
# driver.execute_script("window.scrollTo(0, 400)")
# sleep(1)
# checkboxs[0].click()
# sleep(1)
# checkboxs[1].click()

# Desafio
sleep(2)
botao_desafio = driver.find_element(By.LINK_TEXT, 'Desafios')
sleep(1)
botao_desafio.click()
sleep(1)
driver.execute_script("window.scrollTo(0, 600)")
sleep(1)
conversivel = driver.find_element(By.ID, 'conversivelcheckbox')
sleep(1)
conversivel.click()
sleep(1)
off_road = driver.find_element(By.ID, 'offroadcheckbox')
sleep(1)
off_road.click()
sleep(1)

moto = driver.find_element(By.ID, 'motocheckbox')
if moto.is_selected():
    print('Moto está selecionada')
else:
    print('Moto não está selecionada')


input(' ')
driver.close()