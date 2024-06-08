'''
    Fazer o login na página utilizando a funcionalidades de click e de escrever nos campos
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

# # Passo 1 - Entrar no site 
# driver.get('https://cursoautomacao.netlify.app/')
# sleep(4)

# # Passo 2 - Encontrar o elemento de login e clicar nele
# botao_login = driver.find_element(By.LINK_TEXT, 'Login')
# sleep(1)
# botao_login.click()
# sleep(2)

# # Passo 3 - Encontrar o campo de e-mail e clicar nele
# campo_email = driver.find_element(By.ID, 'email')
# sleep(1)
# campo_email.click()
# sleep(1)

# # Passo 4 - Escrever no campo de e-mail
# campo_email.send_keys('jpsampaio@gmai.com')
# sleep(1)

# # Passo 5 - Encontrar o campo de senha e clicar nele
# campo_senha = driver.find_element(By.NAME, 'campoSenha')
# sleep(1)
# campo_senha.click()
# sleep(2)

# # Passo 6 - Escrever no campo de senha 
# campo_senha.send_keys('minhasenha123')
# sleep(1)

# # Passo 7 - Encontrar e clicar no botão de entrar
# botao_enviar = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
# sleep(1)
# botao_enviar.click()


# Desafio número 2
driver.get('https://cursoautomacao.netlify.app/')
sleep(3)
botao_desafios = driver.find_element(By.LINK_TEXT, 'Desafios')
sleep(1)
botao_desafios.click()
sleep(1)
driver.execute_script("window.scrollTo(0, 350);")
sleep(1)
campo_nome = driver.find_element(By.ID, 'dadosusuario')
sleep(1)
campo_nome.click()
sleep(1)
campo_nome.send_keys('João Paulo Sampaio')
sleep(1)
botao_clique_aqui = driver.find_element(By.ID, 'desafio2')
sleep(1)
botao_clique_aqui.click()
sleep(1)
campo_escondido = driver.find_element(By.XPATH, '//input[@id="escondido"]')
sleep(1)
campo_escondido.click()
sleep(1)
campo_escondido.send_keys('João Paulo Sampaio')
sleep(1)
botao_validar = driver.find_element(By.ID, 'validarDesafio2')
sleep(.5)
botao_validar.click()


input('Digite algo para encerrar a aplicação')
driver.close()