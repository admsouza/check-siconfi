import pandas as pd

# DCA-Anexo I-HI

def d2_1_vpa_fundeb_principal(df):  
    """
    Processa o DataFrame filtrando os dados específicos para VPA.
    """
    # Verificar se o DataFrame está vazio
    if df.empty:
        return "Dado Divergente"

    # Verificar se a coluna 'conta' existe no DataFrame
    if 'conta' not in df.columns:
        return "Dado Divergente"

    # Filtrar o DataFrame onde a coluna 'conta' contém a substring '4.5.2.2.4'
    filtered_df = df[df['conta'].str.contains('4.5.2.2.4', na=False)]

    # Verificar se o DataFrame filtrado está vazio
    if filtered_df.empty:
        return "Dado Divergente"

    # Verificar se a coluna 'valor' existe no DataFrame filtrado
    if not pd.api.types.is_numeric_dtype(filtered_df['valor']):
        return "Dado Divergente"

    # Verificar se algum valor na coluna 'valor' é maior que zero
    if (filtered_df['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"
