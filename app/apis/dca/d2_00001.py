import requests
import pandas as pd
from ...apis.urls import API_DCA

API_URL = API_DCA

def vpa_fundeb_principal(id_ente, an_exercicio):  
    url = f"{API_URL}?an_exercicio={an_exercicio}&id_ente={id_ente}&no_anexo=DCA-Anexo I-HI"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('items', [])
        return process_data(data)
    else:
        return None

def process_data(data):
    if not data:
        return "Dado Divergente"

    # Converte os dados para um DataFrame
    df = pd.DataFrame(data)

    # Filtra as linhas onde a coluna 'conta' contém '4.5.2.2.4'
    filtered_df = df[df['conta'].str.contains('4.5.2.2.4', na=False)]

 # Verifica se existem dados filtrados
    if filtered_df.empty:
        return "Dado Divergente"

    # Verifica se a coluna 'valor' existe
    if 'valor' not in filtered_df.columns:
        return "Dado Divergente"  # Retorna "Dado Divergente" se a coluna não existir

    # Verifica se o valor é maior que zero
    if (filtered_df['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"