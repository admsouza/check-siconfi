import pandas as pd

# DCA-Anexo I-C

def d2_4_receitas_fundeb(df):  
    if df.empty:
            return "Dado Divergente"

    # Verifica se a coluna 'conta' existe no DataFrame
    if 'conta' not in df.columns:
        return "Dado Divergente"  # Retorna "Dado Divergente" se a coluna não existir

    # Filtra as linhas onde a coluna 'conta' contém 'Deduções - FUNDEB'
    filtered_df = df[df['conta'].str.contains('1.7.5.1', na=False)]

    # Verifica se existem dados filtrados
    if filtered_df.empty:
        return "Dado Divergente"

    # Verifica se a coluna 'valor' existe
    if not pd.api.types.is_numeric_dtype(filtered_df['valor']):
        return "Dado Divergente"

    # Verifica se o valor é maior que zero
    if (filtered_df['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"
