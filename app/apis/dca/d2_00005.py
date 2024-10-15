import requests
import pandas as pd
from ...apis.urls import API_DCA  # Verifique se o caminho está correto

API_URL = API_DCA

def desp_patronal_empenhada(id_ente, an_exercicio):
    url = f"{API_URL}?an_exercicio={an_exercicio}&id_ente={id_ente}&no_anexo=DCA-Anexo I-D"
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

    # Verifica se as colunas 'coluna' e 'conta' existem
    if 'coluna' not in df.columns or 'conta' not in df.columns:
        return "Dado Divergente"

    # Filtra apenas as linhas onde 'coluna' contém exatamente 'Despesas Empenhadas'
    df_coluna = df[df['coluna'].str.strip() == 'Despesas Empenhadas']

    # Verifica se há dados após a filtragem
    if df_coluna.empty:
        return "Dado Divergente"

    # Filtra as linhas onde a coluna 'conta' contém exatamente '13'
    filtered_df = df_coluna[df_coluna['conta'].astype(str).str.contains(r'\b13\b', na=False)]

    # Verifica se há dados após a filtragem por '13'
    if filtered_df.empty:
        return "Dado Divergente"

    # Verifica se a coluna 'valor' existe no DataFrame filtrado
    if 'valor' not in filtered_df.columns:
        return "Dado Divergente"

    # Verifica se algum valor é maior que zero
    if (filtered_df['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"

