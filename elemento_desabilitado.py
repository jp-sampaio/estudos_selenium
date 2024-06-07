'''
    Nesse exemplo eu devo encontrar os elementos que estão com a função desabilitado 
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


if __name__ == '__main__':
    driver = iniciar_driver()
    # driver.get('https://cursoautomacao.netlify.app/')
    
    # driver.maximize_window()
    
    # campo_nome = driver.find_element(By.ID, 'campoIdade')
    
    # if campo_nome.is_enabled():
    #     print('O elemento está habilitado!')
        
    # if campo_nome.is_enabled() == False:
    #     print('O elemento está desabilitado!')
        
        
    # Desafio 
    driver.get('https://cursoautomacao.netlify.app/desafios')
    
    botao1 = driver.find_element(By.CSS_SELECTOR, '.btn.btn-info')
    botao2 = driver.find_element(By.XPATH, '//section//button[2]')
    botao3 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-warning')
    
    if botao1.is_enabled():
        print('Botão 1 está habilitado')
    else:
        print('Botão 1 está desabilitado')
        
    if botao2.is_enabled():
        print('Botão 2 está habilitado')
    else:
        print('Botão 2 está desabilitado')
        
    if botao3.is_enabled():
        print('Botão 3 está habilitado')
    else:
        print('Botão 3 está desabilitado')
    
    input('')
    driver.close()