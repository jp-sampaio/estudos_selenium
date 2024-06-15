'''
    ## Implicit wait
    - É usado para informar ao driver da web para esperar um determinado período de tempo antes de lançar uma “Exceção de não tal elemento”. 
    - Ele vai tentar interagir com tal elemento durante esse período que foi determinado
'''

from codigo_padrao import iniciar_driver, By

driver = iniciar_driver()

# Qual elemento apartir de agora vai esperar 10 segundo antes de mostrar um erro, e nesse período vai tentando interagir com o elemento
driver.implicitly_wait(10)

driver.get('https://www.google.com.br/travel/')

travel = driver.find_elements(By.XPATH, '//div[@class="NP08ab"]')

travel[0].click()

input('...')
driver.close()
