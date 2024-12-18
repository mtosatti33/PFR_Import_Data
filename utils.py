import pandas as pd
import os
import glob
import shutil
from pathlib import Path
from config import *
from log import *

# ------------------------------------------------------------------------------------------------
def move_files(_year):
    gen_log()

    for src_file, dest_file in FILES_TO_MOVE.items():
        origem = Path(src_file)
        destino = Path(dest_file.format(_year))

        # Criar diretório de destino (se necessário)
        destino.parent.mkdir(parents=True, exist_ok=True)

        try:
            origem.rename(destino)
            print(f"Arquivo '{src_file}' movido para '{dest_file.format(_year)}'")
        except FileNotFoundError:
            log = f"Arquivo '{src_file}' não encontrado."
            print(log)

            log_error(log)

        except Exception as e:
            log = f"Erro ao mover '{src_file}': {e}"
            print(log)

            log_error(log)

    clean_remaining_data()

# ------------------------------------------------------------------------------------------------   
def move_file(file, destination):
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.move(file, destination)

# ------------------------------------------------------------------------------------------------
def concat_dfs(_file):
    files = glob.glob("*.csv")
    dfs = []

    for file in files:
        df = pd.read_csv(file, sep=';')
        dfs.append(df)
        
    df_new = pd.concat(dfs,ignore_index=True)
    df_new.to_csv(_file, index=False, sep=';')
    
# ------------------------------------------------------------------------------------------------
def create_folders():
    if not os.path.exists('data'):
        for folder in folders:
            create_folder(folder)
        generate_teams_csv()

# ------------------------------------------------------------------------------------------------
def create_folder(folder):
    Path(folder).mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------------------------------------
def clean_remaining_data():
    files = glob.glob("*.csv")
    for file in files:
        os.remove(file)

# ------------------------------------------------------------------------------------------------
def generate_teams_csv():
    df = pd.DataFrame(teams_csv)
    
    df.columns = df.iloc[0]  # Define a segunda linha como cabeçalho
    df = df[1:]  # Exclui as duas primeiras linhas
    df = df.reset_index(drop=True)  # Reseta o índice

    df.to_csv("data/raw/teams.csv", sep=';',index=False)
    