import requests
import pandas as pd
from ...apis.urls import API_DCA

API_URL = API_DCA

def desp_custeio_empenhada(id_ente, an_exercicio):
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

    if df_coluna.empty:
        return "Dado Divergente"

    # Filtra linhas onde 'conta' NÃO contém os termos "Pessoal e Encargos Sociais" e "Juros e Encargos da Dívida"
    contas_excluidas = [
        r'\bPessoal e Encargos Sociais\b',
        r'\bJuros e Encargos da Dívida\b'
    ]
    filtro_conta = ~df_coluna['conta'].str.contains('|'.join(contas_excluidas), case=False, na=False)
    filtered_df = df_coluna[filtro_conta]

    if filtered_df.empty:
        return "Dado Divergente"

    # Verifica se a coluna 'valor' existe e é numérica
    if 'valor' not in filtered_df.columns or not pd.api.types.is_numeric_dtype(filtered_df['valor']):
        return "Dado Divergente"

    # Verifica se algum valor é maior que zero
    if (filtered_df['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"