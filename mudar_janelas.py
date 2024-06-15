'''
    Como podemos alterar as janelas e interagir com as diferentes janelas no navegador
'''

from codigo_padrao import iniciar_driver, By
from time import sleep
from random import randint

driver = iniciar_driver()

def write_smoothly(text, element):
    for row in text:
        element.send_keys(row)
        sleep(randint(1, 9) / 30)

# Abrir o navegador no endereço desejado
driver.get('https://cursoautomacao.netlify.app/')
sleep(3)

# Salvar a janela atual para ser usado depois
current_window = driver.current_window_handle
print(f'Primeira janela {current_window}')

# Fazer um scroll na página para o elemento de abrir uma nova janela
driver.execute_script('window.scrollTo(0, 900);')
sleep(2)

# Encontrar o elemento e clicar no elemento
button_new_window = driver.find_element(By.XPATH, '//button[text()="Abrir Janela"]')
sleep(1)
# Nesse caso a segunda forma de clicar foi mais compatível
driver.execute_script('arguments[0].click()', button_new_window)
sleep(3)

# Quais janelas estão abertas?
windows = driver.window_handles
for window in windows:
    print(window)
    # Mudar o foco para a nova janela
    if window not in current_window:
        # Alterar para essa nova janela
        driver.switch_to.window(window)
        sleep(2)
        # Encontrar o campo de digitar
        search_field = driver.find_element(By.ID, 'campo_pesquisa')
        sleep(1)
        # Escrever uma pesquisa
        write_smoothly('Meus animes', search_field)
        sleep(2)
        # Encontrar o botão de pesquisa
        search_button = driver.find_element(By.ID, 'fazer_pesquisa')
        sleep(1)
        # Clicar no campo de pesquisa
        search_field.click()
        sleep(3)
        # Fechar a nova janela
        driver.close()

# Alterando para a janela inicial
driver.switch_to.window(current_window)
sleep(2)

driver.close()
input('Concluído!')
