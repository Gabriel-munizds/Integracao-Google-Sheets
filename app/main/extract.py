import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Define Usuário e Senha do SIAC
usuario = '<LOGIN>'
senha = '<SENHA>'

# Define Período do relatório (ddmmaa)
initialDate = '01012023' 
finalDate = '31012023'
# Configura o caminho para o driver do navegador
chromedriver_path = '/chromedriver/chromedrive.exe'

# Define as opções do navegador para fazer o download sem perguntar o local do arquivo
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

browser = webdriver.Chrome(service=Service(executable_path=chromedriver_path), options=options)# Abre o navegador com as opções configuradas

#------------------------------------------LOGIN------------------------------------------------------------------
# Acessa a página onde o arquivo está localizado
browser.get('http://www.siacweb.com.br/')
time.sleep(3)

# Passando usuário
TextLogin = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/form/table/tbody/tr[2]/td[2]/input')
TextLogin.send_keys(usuario)
time.sleep(1)

# Passando Senha
TextPassWord = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input[1]')
TextPassWord.send_keys(senha)
time.sleep(1)

# Clicando "fazer login"
SubmitButton = browser.find_element(by=By.CSS_SELECTOR, value='#ok')
SubmitButton.click()
time.sleep(1)


#----------------------------------CAMINHO PARA O ARQUIVO-----------------------------------------------------
browser.get('http://www.siacweb.com.br/relatorios.php?tipo=relatorio_vendas_csv')
time.sleep(3)

# Inserindo Data Inicial
initialDateText = browser.find_element(by=By.XPATH, value='/html/body/form/table/tbody/tr[2]/td[2]/span/input')
initialDateText.send_keys(initialDate)
time.sleep(1)

# Inserindo Data final
finalDateText = browser.find_element(by=By.XPATH, value='/html/body/form/table/tbody/tr[4]/td[2]/span/input')
finalDateText.send_keys(finalDate)
time.sleep(1)

#limpando tela de pop ups
SubmitButton1 = browser.find_element(by=By.XPATH, value='/html/body')
SubmitButton1.click()
time.sleep(1)


# Clicando "Baixar Relatório"
SubmitButton2 = browser.find_element(by=By.XPATH, value='/html/body/form/table/tbody/tr[5]/td[2]/div/input')
SubmitButton2.click()

# Aguarda o download ser concluído
time.sleep(20)

# Encontra o nome do arquivo baixado no diretório de downloads do navegador
download_directory = 'C:/Users/ESCRITORIO PA/Downloads'
for file in os.listdir(download_directory): # <---- PENSAR EM UMA ESTRATÉGIA MELHOR
    if file.find('docs_relatorio_vendas'):  # ou a extensão do arquivo desejado
        file_name = file
        break

# Move o arquivo baixado para o diretório desejado em seu sistema
if file_name is not None:
    os.rename(os.path.join(download_directory, file_name), os.path.join('C:/Users/ESCRITORIO PA/Desktop/Integracao-Google-Sheets/app/main/data_base', file_name))




browser.quit()
