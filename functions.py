import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import glob
import logging
from datetime import datetime
from pathlib import Path

from folders import *
from moving_list import *
# Funções
# ------------------------------------------------------------------------------------------------
def scraping_data(url, attrs, file, is_data_append_csv = False, is_append_team = False, data_show=None):
    driver = webdriver.Chrome()
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
        df["Team"] = file
        
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

def move_files():
    nome_arquivo = 'log.txt'

    logging.basicConfig(
        filename=nome_arquivo,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'
    )
    for src_file, dest_file in FILES_TO_MOVE.items():
        origem = Path(src_file)
        destino = Path(dest_file)

        # Criar diretório de destino (se necessário)
        destino.parent.mkdir(parents=True, exist_ok=True)

        try:
            origem.rename(destino)
            print(f"Arquivo '{src_file}' movido para '{dest_file}'")
        except FileNotFoundError:
            log = f"Arquivo '{src_file}' não encontrado."
            print(log)

            logging.error(log)

        except Exception as e:
            log = f"Erro ao mover '{src_file}': {e}"
            print(log)

            logging.error(log)
                


# ------------------------------------------------------------------------------------------------
def concat_dfs():
    files = glob.glob("*.csv")
    dfs = []

    for file in files:
        df = pd.read_csv(file, sep=';')
        dfs.append(df)
        
    df_new = pd.concat(dfs,ignore_index=True)
    df_new.to_csv("rosters.csv", index=False, sep=';')
    
# ------------------------------------------------------------------------------------------------
def recreate_folders():
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True) 

def clean_remaining_data():
    files = glob.glob("*.csv")
    for file in files:
        os.remove(file)