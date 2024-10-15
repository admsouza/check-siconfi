import requests
import pandas as pd
from ...apis.urls import API_DCA

API_URL = API_DCA

def desp_por_funcao(id_ente, an_exercicio):
    url = f"{API_URL}?an_exercicio={an_exercicio}&id_ente={id_ente}&no_anexo=DCA-Anexo I-E"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json().get('items', [])
        return process_data(data)
    else:
        return "Dado Divergente"

def process_data(data):
    if not data:
        return "Dado Divergente"

    # Converte os dados para um DataFrame
    df = pd.DataFrame(data)

    # Verifica se as colunas 'conta' e 'valor' existem
    if 'conta' not in df.columns or 'valor' not in df.columns:
        return "Dado Divergente"

    # Filtra linhas onde 'conta' não está vazia
    df_conta = df[df['conta'].notna() & df['conta'].str.strip().astype(bool)]

    if df_conta.empty:
        return "Dado Divergente"

    # Verifica se a coluna 'valor' é numérica
    if not pd.api.types.is_numeric_dtype(df_conta['valor']):
        return "Dado Divergente"

    # Verifica se algum valor é maior que zero
    if (df_conta['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"