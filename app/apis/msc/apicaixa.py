import requests
import pandas as pd
from ...apis.urls import API_MSC_PAT

API_URL = API_MSC_PAT

def get_api_caixa(id_ente, an_referencia):
    # Montando a URL completa com os parâmetros
    url = f"{API_URL}?id_ente={id_ente}&an_referencia={an_referencia}&me_referencia=1&co_tipo_matriz=MSCC&classe_conta=1&id_tv=ending_balance"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json().get('items', [])
        return process_data(data)
    else:
        return None

def process_data(data):
    if not data:
        return None

    # Converte os dados para um DataFrame
    df = pd.DataFrame(data)

    # Verifica se as colunas necessárias estão presentes
    required_columns = ['valor', 'data_referencia', 'conta_contabil', 'natureza_conta', 'tipo_valor']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        return None

    # Limpar e preparar os dados
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df['data_referencia'] = pd.to_datetime(df['data_referencia'], errors='coerce')

    # Filtrar os dados para natureza C
    filtered_C = df[
        (df['conta_contabil'].str.contains("11111")) & 
        (df['natureza_conta'] == "C") & 
        (df['tipo_valor'] == "ending_balance")
    ]

    # Filtrar os dados para natureza D
    filtered_D = df[
        (df['conta_contabil'].str.contains("11111")) & 
        (df['natureza_conta'] == "D") & 
        (df['tipo_valor'] == "ending_balance")
    ]

    # Calcular os totais somados
    total_C = filtered_C['valor'].sum()
    total_D = filtered_D['valor'].sum()

    # Subtrair o total de C do total de D
    resultado = total_D - total_C
    return resultado

# Verificar se o valor do caixa é maior que zero

def dado_final(resultado):
    if resultado == 0:
        return "Dado Consistente"
    else:
        return "Dado Divergente"
