def Req():

    import requests
    from bs4 import BeautifulSoup as sp



    page = requests.get('https://www.python.org/')
    soup = sp(page.content, 'html.parser')
    soup.find('span', {'class': 'massege'}).text


def Sel():

    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Define o caminho do driver do navegador (Chrome)
    driver_path = '/html/body/section/article/section[2]/div[253]/div/div/div[1]/div/div/div[2]/span/a'

    # Inicializa o driver do navegador
    driver = webdriver.Chrome(executable_path=driver_path)

    # Define a URL para abrir no navegador
    url = 'https://www.transvias.com.br/transportadoras/estados/sao-paulo'

    # Abre a URL no navegador
    driver.get(url)

    # Localiza o elemento do título na página usando um seletor CSS
    title_element = driver.find_element(By.CSS_SELECTOR, 'body > section > article > section.l-sectionMap__results__companies > div:nth-child(254) > div > div > div.m-boxCompany__A > div > div > div:nth-child(4)')

    # Extrai o texto do elemento do título
    title_text = title_element.text

    # Imprime o título da página
    print(title_text)

    # Fecha o navegador
    driver.quit()


def Sel1():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Define o caminho do driver do navegador (Chrome)
    driver_path = '/path/to/chromedriver'

    # Inicializa o driver do navegador
    driver = webdriver.Chrome(executable_path=driver_path)

    # Define a URL para abrir no navegador
    url = 'https://www.transvias.com.br/transportadoras/estados/sao-paulo'

    # Abre a URL no navegador
    driver.get(url)

    # Espera até que os elementos estejam presentes na página
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="conteudo_coluna2"]/div[contains(@class, "caixaTransportadora")]'))
    )

    # Extrai o nome e a descrição de cada transportadora na página
    for element in elements:
        name = element.find_element(By.XPATH, './/h2').text
        description = element.find_element(By.XPATH, './/p').text
        print('Name:', name)
        print('Description:', description)
        print('---')

    # Fecha o navegador
    driver.quit()


def Sel2():

    import requests as rq
    from bs4 import BeautifulSoup


    headers = {'user-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

    site = rq.get('https://www.guiadotransporte.com.br/transportadoras/maringa-pr?page=1', headers=headers)
    status = site.status_code

    if status == 200:
        print('ok')

        soup = BeautifulSoup(site.content, 'html.parser')
        trp = soup.find_all('div', class_='row')

        email = trp.find_all('a', class_='email')

        print(email)

    else:
        print('não está conectado ao site')


def CotacaoDolar():

    import requests as rq
    from bs4 import BeautifulSoup

    headers = {'user-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}


    dolar = rq.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+do+dolar&rlz=1C1BNSD_pt-BRBR1044BR1044&oq=cota%C3%A7%C3%A3o+do+dolar&aqs=chrome..69i57j0i433i457i512j0i402i512j0i402i433i512j0i512l6.5836j1j15&sourceid=chrome&ie=UTF-8', headers=headers)
    soup  = BeautifulSoup(dolar.content, 'html.parser')
    cotacao = soup.find('span', class_='DFlfde SwHCTb').get_text()


    print(cotacao)


def SelGpt():

    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.guiadotransporte.com.br/transportadoras/maringa-pr?page=1'

    # Faz a requisição HTTP para obter o HTML da página
    response = requests.get(url)

    # Analisa o HTML usando a biblioteca BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Procura por todos os links com a classe "mail-link"
    mail_links = soup.find_all('a', class_='email')

    # Extrai o e-mail de cada link encontrado
    emails = [link['href'].replace('mailto:', '') for link in mail_links]

    # Imprime os e-mails encontrados
    print(emails)


def SelGpt1():

    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.guiadotransporte.com.br/transportadoras/maringa-pr?page=1'

    # Faz a requisição HTTP para obter o HTML da página
    response = requests.get(url)

    # Analisa o HTML usando a biblioteca BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Procura por todos os links com a classe "mail-link"
    mail_links = soup.find_all('a', class_='email')

    # Extrai o e-mail de cada link encontrado
    emails = [link['href'].replace('mailto:', '') for link in mail_links]

    # Imprime os e-mails encontrados
    print(emails)


def SelGpt2():

    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.guiadotransporte.com.br/transportadoras/maringa-pr?page=6'

    # Faz a requisição HTTP para obter o HTML da página
    response = requests.get(url)

    # Analisa o HTML usando a biblioteca BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Procura por todos os links com a classe "whatsapp-link"
    whatsapp_links = soup.find_all('a', target='_blank')

    # Extrai o número de WhatsApp de cada link encontrado
    numbers = [link['href'].replace('https://api.whatsapp.com/send?phone=', '') for link in whatsapp_links]

    # Imprime os números de WhatsApp encontrados
    print(numbers)


SelGpt2()