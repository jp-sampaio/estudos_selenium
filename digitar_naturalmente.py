'''
    Digitar nos campos de forma humanizada, com tempos aleatórios e pausas
'''

from codigo_padrao import iniciar_driver, By
from time import sleep
from random import randint

# Inicializar a lista que irá armazenar as linhas do arquivo
paragrafo = []

# Abrir o arquivo e ler linha por linha
with open('texto.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        paragrafo.append(linha.strip())  # Remover espaços em branco (incluindo novas linhas) nas extremidades de cada linha

# Unir todas as linhas em uma única string
texto = ' '.join(paragrafo)  # Você pode usar qualquer delimitador desejado, aqui é um espaço


def escrever_texto(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 5) / 30)

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
sleep(2)
# Maximizar a tela afim de ter uma visualização melhor 
driver.maximize_window()
sleep(1)
# # Scroll na tela para chegar no elemento da tela que eu quero
# driver.execute_script("window.scrollTo(0, 300);")
# sleep(1)
# # Pegando o elemento da tela 
# campo_paragrafo = driver.find_element(By.XPATH, '//textarea[@placeholder="digite seu texto aqui"]')
# sleep(1)
# campo_paragrafo.click()
# sleep(1)

# # Digitar na tela de forma humanizada
# escrever_texto(texto, campo_paragrafo)


# Desafio 
campo_desafio = driver.find_element(By.LINK_TEXT, 'Desafios')
sleep(1)
campo_desafio.click()
sleep(1)
driver.execute_script("window.scrollTo(0, 800);")
sleep(1)
text_area = driver.find_element(By.ID, 'campoparagrafo')
sleep(1)
text_area.click()
sleep(1)
escrever_texto(texto, elemento=text_area)


input('Automação Encerrada!')
driver.close()
