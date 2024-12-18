import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import requests

from config import *
# Funções
# ------------------------------------------------------------------------------------------------
def scraping_data(url, attrs, file, is_data_append_csv = False, is_append_team = False, data_show=None):
    print(f'Scraping {file} from link {url}')
    # Configurar o WebDriver (exemplo com Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    
    url = url
    driver.get(url)
    time.sleep(2)

    # Lista para armazenar os dados
    lista = []
        
    if data_show is not None:
        click_element(driver, data_show)
        
    rows = driver.find_elements(By.XPATH, f'//*[contains(@id,"{attrs}")]//tr[not(contains(@class, "over_header"))]')

    # Iterar pelas linhas da tabela
    for row in rows:
        # Capturar os dados da linha
        data = [item.text for item in row.find_elements(By.XPATH, ".//*[self::td or self::th]")]
        
        # Capturar o link (se existir) do jogador
        if is_data_append_csv:
            # data-append-csv
            append_csv = row.find_elements(By.XPATH, ".//td[@data-append-csv]")
            player_id = append_csv[0].get_dom_attribute('data-append-csv') if append_csv else ""
        
        # Adicionar o identificador ao final da linha de dados
        if data:  # Evitar adicionar linhas vazias
            if is_data_append_csv:
                if len(lista) == 0:
                    data.append('Player-additional')
                else:
                    data.append(player_id)

            lista.append(data)

    # Converter os dados para um DataFrame
    df = pd.DataFrame(lista)
    
    df.columns = df.iloc[0]  # Define a segunda linha como cabeçalho
    df = df[1:]  # Exclui as duas primeiras linhas
    df = df.reset_index(drop=True)  # Reseta o índice

    if is_append_team:
        df["Team"] = file.split('.')[0]
        
    # Exclui duplicadas
    df = df.drop_duplicates()

    # Salvar como CSV
    df.to_csv(file, index=False, sep=';')
    
    driver.quit()

# ------------------------------------------------------------------------------------------------
def click_element(driver, attr):
    try:
        selector = f"a[data-show='{attr}']"
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        driver.execute_script("arguments[0].click();", element)
        print(f"Elemento com 'data-show={attr}' clicado via JavaScript!")
    except Exception as e:
        print(f"Erro ao clicar no elemento com 'data-show={attr}': {e}")

# ------------------------------------------------------------------------------------------------
def download_logo(url, _team = None):
    # Configurar o WebDriver (exemplo com Chrome)
    driver = webdriver.Chrome()

    # Abrir a URL da página
    url_pagina = url
    driver.get(url_pagina)

    # Localizar o elemento da imagem pelo seletor de classe
    try:
        # Localiza o elemento da imagem
        img_element = driver.find_element(By.XPATH, "//img[@class='teamlogo']")
        
        # Extrai o URL da imagem (atributo 'src')
        img_url = img_element.get_attribute("src")
        print(f"URL da imagem: {img_url}")

        # Nome do arquivo local
        if _team is not None:
            nome_arquivo = f"{_team}.png"
        else:
            nome_arquivo = "NFL.png"

        diretorio = TEAM_LOGOS
        os.makedirs(diretorio, exist_ok=True)  # Cria o diretório, se necessário

        caminho_completo = os.path.join(diretorio, nome_arquivo)

        # Fazer o download da imagem
        response = requests.get(img_url, stream=True)
        response.raise_for_status()  # Verifica se houve erro no download
        
        with open(caminho_completo, "wb") as file:
            for chunk in response.iter_content(1024):  # Salva em pedaços
                file.write(chunk)

        print(f"Imagem salva em: {caminho_completo}")
        
    except Exception as e:
        print(f"Erro ao baixar a imagem: {e}")

    # Fechar o navegador
    driver.quit()