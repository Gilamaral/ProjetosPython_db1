def User():

    import PySimpleGUI as sg

    # Define o usuário e senha
    usuario = "teste"
    senha = "teste"

    # Cria a interface gráfica
    layout = [
        [sg.Text("Usuário:"), sg.Input(key="usuario", size=(20, 1))],
        [sg.Text("Senha:"), sg.Input(key="senha", size=(20, 1), password_char="*")],
        [sg.Button("Login"), sg.Button("Cancelar")]
    ]

    janela = sg.Window("Login", layout, element_justification="c")

    # Loop principal
    while True:
        evento, valores = janela.read()

        # Verifica se o usuário clicou no botão "Cancelar" ou fechou a janela
        if evento == sg.WINDOW_CLOSED or evento == "Cancelar":
            break

        # Verifica se o usuário e senha estão corretos
        if valores["usuario"] == usuario and valores["senha"] == senha:
            sg.popup("Login bem-sucedido!", title="Login")
            break
        else:
            sg.popup("Usuário ou senha incorretos.", title="Login", icon="ERROR")
            janela["usuario"].update("")
            janela["senha"].update("")
            janela["usuario"].set_focus()


def Xml():

    import xml.etree.ElementTree as ET

    # caminho do arquivo XML que você deseja ler
    caminho_arquivo = "caminho/do/arquivo.xml"

    # criar um objeto ElementTree a partir do arquivo XML
    arvore = ET.parse(caminho_arquivo)

    # obter o elemento raiz do arquivo XML
    raiz = arvore.getroot()

    # acessar e imprimir o texto do primeiro elemento filho da raiz
    print(raiz[0].text)


def WhatsGpt():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time

    # Crie uma instância do driver do Chrome
    driver = webdriver.Chrome()

    # Abra o WhatsApp Web e faça o login na sua conta do WhatsApp
    driver.get("https://web.whatsapp.com")

    while len(driver.find_elements(By.ID,"side")) < 1:
        time.sleep(1)

    numcont = str('554498741886')
    msg = 'consegui programar'

    time.sleep(3)

    # Encontre o campo de pesquisa e digite o nome ou número do contato
    contato = None
    while not contato:
        try:
            contato = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            contato.send_keys(numcont)
            time.sleep(2)
            contato.send_keys(Keys.ENTER)
        except:
            pass

    # Localize o campo de texto e digite a mensagem
    campo_mensagem = None
    while not campo_mensagem:
        try:
            campo_mensagem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            campo_mensagem.send_keys(msg)
            time.sleep(2)
        except:
            pass

    # Encontre o botão "Enviar" e clique nele
    botao_enviar = None
    while not botao_enviar:
        try:
            botao_enviar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            botao_enviar.click()
            time.sleep(2)
        except:
            pass

    # Encerre o navegador
    driver.quit()



def wixGpt():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time

    # Crie uma instância do driver do Chrome
    driver = webdriver.Chrome()

    # Abra o WhatsApp Web e faça o login na sua conta do WhatsApp
    driver.get("https://www.apptruckar.com.br/")


    numcont = str('Gilvan')
    msg = 'amaralgilvan16@gmail.com'

    time.sleep(6)


    chat = None
    while not chat:
        try:
            chat = driver.find_element(By.XPATH, '//*[@id="maximized-chat"]')
            chat.click()
        except:
            pass
    
    
'''
    # Encontre o campo de pesquisa e digite o nome ou número do contato
    contato = None
    while not contato:
        try:
            contato = driver.find_element(By.XPATH, '//*[@id="name"]')
            contato.send_keys(numcont)
            time.sleep(2)
            contato.send_keys(Keys.ENTER)
        except:
            pass

    # Localize o campo de texto e digite a mensagem
    campo_mensagem = None
    while not campo_mensagem:
        try:
            campo_mensagem = driver.find_element(By.XPATH, '//*[@id="email"]')
            campo_mensagem.send_keys(msg)
            time.sleep(2)
        except:
            pass

    # Encontre o botão "Enviar" e clique nele
    botao_enviar = None
    while not botao_enviar:
        try:
            botao_enviar = driver.find_element(By.XPATH, '//*[@id="chat-messages-list"]/div[4]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/form/button')
            botao_enviar.click()
            time.sleep(2)
        except:
            pass

    # Encerre o navegador
    driver.quit()
'''

wixGpt()