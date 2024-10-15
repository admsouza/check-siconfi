import requests
import pandas as pd
from ...apis.urls import API_DCA

API_URL = API_DCA

def receitas_outros_entes(id_ente, an_exercicio):
    url = f"{API_URL}?an_exercicio={an_exercicio}&id_ente={id_ente}&no_anexo=DCA-Anexo I-C"
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

    # Filtra as contas onde o segundo número é "7"
    df_conta = df[df['conta'].str.match(r'^\d\.7\.', na=False)]

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