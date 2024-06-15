'''
    Desafio de número 7: Ir na página desafios, digitar o que estou achando do curso, depois voltar para a página anterior e digitar algo no campo definido.
'''

# Libs
from codigo_padrao import iniciar_driver, By
from time import sleep
from random import randint


# Funções e váriavéis 

# Função onde se escreve de forma humana
def write_smoothly(text, element):
    for row in text:
        element.send_keys(row)
        sleep(randint(1, 9) / 30)

comment = 'O curso realmente é muito incrível, estou aprendendo muitas coisas que nunca imaginei aprender antes e espero continuar evoluindo muito ainda.'
conclusion = 'Concluindo a automação, foi incrível esse aprendizado que vai serve para muitas outras coisas no futuro.'

# Inicializando a automação

# Inicializar o driver do navegador
driver = iniciar_driver()

# Abrir a página do navegador
driver.get('https://cursoautomacao.netlify.app/')
sleep(4)
# Definir a página inicial
home_page = driver.current_window_handle
# Link da página de desafios 
challenges = driver.find_element(By.LINK_TEXT, 'Desafios')
sleep(2)
# Clicar no link que leva para a página de desafios
challenges.click()
sleep(3)
# Scrollar a página até o elemento de abrir uma nova janela
driver.execute_script('window.scrollTo(0, 2500);')
sleep(2)
# Botão que abre uma nova janela
open_new_window_button = driver.find_element(By.XPATH, '//button[text()="Abrir nova janela"]')
sleep(1)
# Clicar no botão de abrir nova janela
driver.execute_script('arguments[0].click()', open_new_window_button)
sleep(3)
# Verificar quais as janelas estão abertas no momento
windows = driver.window_handles
for window in windows:
    if window not in home_page:
        # Mudar o foco para essa nova janela
        driver.switch_to.window(window)
        # Campo de texto onde vou inserir meu comentário sobre o curso
        comment_field = driver.find_element(By.ID, 'opiniao_sobre_curso')
        sleep(1)
        # Escrever no campo de comentário
        write_smoothly(comment, comment_field)
        sleep(2)
        # Botão de pesquisa que envia o meu comentário
        search_button = driver.find_element(By.ID, 'fazer_pesquisa')
        sleep(2)
        # Clicar no campo de pesquisa
        search_button.click()
        sleep(1)
        # Fechar a janela nova
        driver.close()

# Mudar o foco para a janela inicial
driver.switch_to.window(home_page)
sleep(1)
# Campo de texto do desafio 7
text_field = driver.find_element(By.ID, 'campo_desafio7')
sleep(3)
# Escrever no campo do desafio 7
write_smoothly(conclusion, text_field)
sleep(2)
# Fechar a janela no navegador
driver.close()
input('Concluído!')
