'''
    Utilizando o wait explicito diz ao WebDriver uma condição (ou tempo) para que ele aguarde antes de prosseguir com o teste.
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pr-BR', '--window-size=1300,1000', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait


driver, wait = iniciar_driver()

# driver.get('https://google.com/travel')

# Esperar até todos os elementos forem localizados então faça alguma coisa de acordo com os parâmetros que foram passado no wait
# travel_suggestion = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, '//div[@class="NP08ab"]')))
# travel_suggestion[0].click()

# Esperar até qualquer um dos elementos for localizado então faça alguma coisa de acordo com os parâmetros que foram passado no wait
# travel_suggestion = wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, '//div[@class="NP08ab"]')))
# travel_suggestion[0].click()

driver.get('https://cursoautomacao.netlify.app/login')
sleep(2)

email_field = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//input[@id="email"]')))
email_field.send_keys('jpsampaio@gmail.com')

input('...')
driver.close()
