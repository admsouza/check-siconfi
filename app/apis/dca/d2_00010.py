import pandas as pd

# DCA-Anexo I-C

def d2_10_receitas_outros_entes(df):
    
    if df.empty:
        return "Dado Divergente"
    
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