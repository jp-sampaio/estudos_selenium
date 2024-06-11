'''
    Subir algum arquivo do meu computador para a internet
'''

from codigo_padrao import iniciar_driver, By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Obs: Pausar de forma aleatória cada interação na página

driver = iniciar_driver()
# Entrar na página web
driver.get('https://cursoautomacao.netlify.app/')
sleep(3)
driver.maximize_window()
sleep(1)
# Scroll na página até o elemento que quero interagir
driver.execute_script('window.scrollTo(0, 1900);')
sleep(1)
# Buscar o elemento de upload
upload = driver.find_element(By.XPATH, "//input[@id='myFile']")
sleep(1)
# Escrever o caminho do arquivo que quero subir, melhor do que clicar no campo para escolher o arquivo clicando nos campos.
upload.send_keys('C:\\Users\\jpsam\\OneDrive\\Documentos\\curso_python\\bot_whatsapp\\assets\\iniciar.png')
sleep(2)
# Buscar o elemento de enviar o arquivo
enviar_arquivo = driver.find_element(By.XPATH, '//input[@value="Enviar Arquivo"]')
sleep(1)
# Clicar no elemento de enviar o arquivo
enviar_arquivo.click()

input('Automação concluída!')
driver.close()
