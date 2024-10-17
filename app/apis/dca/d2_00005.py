import pandas as pd

# DCA-Anexo I-D
def d2_5_desp_patronal_empenhada(df):

    if df.empty:
            return "Dado Divergente"

    # Verifica se a coluna 'conta' existe no DataFrame
    if 'conta' not in df.columns:
        return "Dado Divergente"  # Retorna "Dado Divergente" se a coluna não existir

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
    if not pd.api.types.is_numeric_dtype(filtered_df['valor']):
        return "Dado Divergente"

    # Verifica se algum valor é maior que zero
    if (filtered_df['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"

