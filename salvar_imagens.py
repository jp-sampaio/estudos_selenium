'''
    Salvando imagens do site, seja apenas uma foto ou várias delas
'''

from codigo_padrao import iniciar_driver, By
from time import sleep

driver = iniciar_driver()
# driver.get('https://pt.wikipedia.org/wiki/Brasil')
# sleep(2)
# bandeira = driver.find_element(By.XPATH, '//img[@alt="Bandeira do Brasil"]')
# sleep(1)

# # Vai escrever em formato binário a imagem com o nome que foi passado
# with open('bandeira.jpg', 'wb') as arquivo:
#     arquivo.write(bandeira.screenshot_as_png)


# Salvando mais de uma imagem
driver.get('https://cursoautomacao.netlify.app/')
sleep(2)
driver.maximize_window()
sleep(1)
driver.execute_script('window.scrollTo(0, 1600);')
sleep(1)
images = driver.find_elements(By.XPATH, '//img[@class="img-thumbnail"]')
sleep(1)

# Nomeando várias imagens com nomes diferentes 
contador = 1
for image in images:
    with open(f'./images/image{contador}.jpg', 'wb') as arquivo:
        arquivo.write(image.screenshot_as_png)
        sleep(1)
    contador += 1


input('Automação finalizada!')
driver.close()