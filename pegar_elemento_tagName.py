'''
    Pegar um elemento pela sua tag name e com isso posso pecorrer um mais elementos dependendo da quantidade deles no arquivo html
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=600,400', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'downloads.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')

titulo1 = driver.find_element(By.TAG_NAME, 'h1')
titulo4 = driver.find_element(By.TAG_NAME, 'h4')

if titulo1:
    print('Elemento encontrado!')

if titulo4:
    print('Elemento encontrado!')

driver.close()