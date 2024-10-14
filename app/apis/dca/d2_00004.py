import requests
import pandas as pd
import logging
from ...apis.urls import API_DCA

# Configurando o logging
logging.basicConfig(level=logging.INFO)

API_URL = API_DCA

def receitas_fundeb(id_ente, an_exercicio):  
    url = f"{API_URL}?an_exercicio={an_exercicio}&id_ente={id_ente}&no_anexo=DCA-Anexo I-C"

    logging.info(f"Chamando API com a URL: {url}")
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('items', [])
        return process_data(data)
    else:
        logging.error(f"Erro ao acessar a API: {response.status_code}")
        return "Dado Divergente"  # Retorna "Dado Divergente" se a API falhar

def process_data(data):
    if not data:
        logging.warning("Nenhum dado recebido.")
        return "Dado Divergente"  # Retorna "Dado Divergente" se não houver dados

    # Converte os dados para um DataFrame
    df = pd.DataFrame(data)

    # Verifica se a coluna 'conta' existe no DataFrame
    if 'conta' not in df.columns:
        logging.warning("Coluna 'conta' não encontrada nos dados.")
        return "Dado Divergente"  # Retorna "Dado Divergente" se a coluna não existir

    # Filtra as linhas onde a coluna 'conta' contém 'Deduções - FUNDEB'
    filtered_df = df[df['conta'].str.contains('1.7.5.1', na=False)]

    # Verifica se existem dados filtrados
    if filtered_df.empty:
        logging.warning("Nenhum dado consistente encontrado após filtragem.")
        return "Dado Divergente"

    # Verifica se a coluna 'valor' existe
    if 'valor' not in filtered_df.columns:
        logging.warning("Coluna 'valor' não encontrada nos dados filtrados.")
        return "Dado Divergente"  # Retorna "Dado Divergente" se a coluna não existir

    # Verifica se algum valor é maior que zero
    if (filtered_df['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"
