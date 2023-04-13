from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time

def abrir_whatsapp_web():
    # Abre o navegador e entra no WhatsApp Web
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    input("Faça o login no WhatsApp Web e pressione Enter para continuar...")

    return driver

def selecionar_contato(driver, nome_contato):
    # Espera até que a lista de contatos seja carregada
    WebDriverWait(driver, 30).until(visibility_of_element_located((By.XPATH, "//div[@class='_2heX1']")))

    # Seleciona o contato para o qual enviar a mensagem
    contato_xpath = f"//span[@title='{nome_contato}']"
    contato = driver.find_element_by_xpath(contato_xpath)
    contato.click()

    # Espera até que o campo de mensagem seja carregado
    WebDriverWait(driver, 10).until(visibility_of_element_located((By.XPATH, "//div[@class='_2S1VP copyable-text selectable-text']")))

    return driver.find_element_by_xpath("//div[@class='_2S1VP copyable-text selectable-text']")

def enviar_mensagem(driver, campo_mensagem, mensagem):
    # Digita a mensagem e envia
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)

    # Espera alguns segundos para a mensagem ser enviada
    time.sleep(2)

def fechar_whatsapp_web(driver):
    # Fecha o navegador
    driver.quit()

# Exemplo de uso
driver = abrir_whatsapp_web()
contato = 'Dulcy'
msg = 'teste'
campo_mensagem = selecionar_contato(driver, contato)
enviar_mensagem(driver, campo_mensagem, msg)
#fechar_whatsapp_web(driver)


