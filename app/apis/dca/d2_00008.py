# DCA-Anexo I-E

import pandas as pd

def d2_8_desp_por_funcao(df):

    if df.empty:
        return "Dado Divergente"
    
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