'''
    Entendendo o funcionamento do radios e como clicar e saber se ele está selecionado
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
sleep(2)
botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')
sleep(1)
botao_windows.click()
sleep(3)
if botao_windows.is_selected():
    print('O botão está selecionado!')

# Pegando mais de um elemento, retorna uma lista
botoes_radios = driver.find_elements(By.XPATH, '//input[@type="radio"]')
for botao in botoes_radios:
    botao.click()
    sleep(2)


input('Alguma coisa')
driver.close()