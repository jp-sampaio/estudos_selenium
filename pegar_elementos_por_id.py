'''
    Uma das maneiras de pegar um elemento da DOM é pelo o seu ID
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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
botao = driver.find_element(By.ID, 'buttonalerta') # Pega um elemento
botoes = driver.find_elements(By.ID, 'buttonalerta') # Pega mais de um elemento

if botao is not None:
    print('O botão foi encontrado!')

if botoes is not None:
    print('Os botões foram encontrados!')

input('')
driver.close()