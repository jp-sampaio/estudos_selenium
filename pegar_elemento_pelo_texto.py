'''
    Uma das maneiras de pegar um elemento da DOM é pela texto do link ou por um texto parcial do link
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

home = driver.find_element(By.LINK_TEXT, 'Home')
# De um fragmento do texto eu consigo encontrar o elemento 
link_parcial_desafio = driver.find_element(By.PARTIAL_LINK_TEXT, 'Des')

if home is not None:
    print('O elemento home foi encontrado!')

if link_parcial_desafio is not None:
    print('O elemento desafio foi encontrado do fragmento des.')

input('')
driver.close()