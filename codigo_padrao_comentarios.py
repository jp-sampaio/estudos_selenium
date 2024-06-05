'''
    App utilizando as bibliotecas selenium e webdriver-manager afim de automatizar processos web
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e
# https://peter.sh/experiments/chromium-command-line-switches/

# Definir opções de inicialização do chrome
chrome_options = Options()
# Essa são algumas das opções que posso setar
'''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
'''
# Definindo os que vou utilizar
arguments = ['--lang=pt-BR', '--window-size=800, 800', '--incognito']
# Adicionar eles no meu chrome_options
for argument in arguments:
    chrome_options.add_argument(argument)

# Lista de opções experimentais(nem todas estão documentadas) 
# https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
# Uso de configurações experimentais
chrome_options.add_experimental_option('prefs', {
    # Alterar o local padrão de download de arquivos
    'download.default_directory': 'C:\\Users\\jpsam\\OneDrive\\Documentos\\curso_python\\estudos_selenium\\downloads',
    # Notificar o google chrome sobre essa alteração é utilizado em conjunto com o de cima
    'download.directory_upgrade': True,
    # Desabilitar a confirmação de download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # Permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,
})

# Inicializando o webdriver e instalando a versão do driver mais recente do navegador
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options) 
driver.get('https://facebook.com')
input('Digite alguma tecla para encerrar a aplicação.')