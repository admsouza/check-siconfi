import pandas as pd

# DCA-Anexo I-D
def d2_7_desp_custeio_empenhada(df):

    if df.empty:
        return "Dado Divergente"

    # Verifica se as colunas 'coluna' e 'conta' existem no DataFrame
    if 'coluna' not in df.columns or 'conta' not in df.columns:
        return "Dado Divergente"

    # Filtra apenas as linhas onde 'coluna' contém exatamente 'Despesas Empenhadas'
    df_coluna = df[df['coluna'].str.strip() == 'Despesas Empenhadas']

    # Verifica se há dados após a filtragem
    if df_coluna.empty:
        return "Dado Divergente"

    # Exclui entradas onde a coluna 'conta' contém os termos "Pessoal e Encargos Sociais" e "Juros e Encargos da Dívida"
    contas_excluidas = ['Pessoal e Encargos Sociais', 'Juros e Encargos da Dívida']
    df_filtrado = df_coluna[~df_coluna['conta'].str.contains('|'.join(contas_excluidas), na=False)]

    # Verifica se há dados após a filtragem
    if df_filtrado.empty:
        return "Dado Divergente"

     # Verifica se a coluna 'valor' existe no DataFrame filtrado
    if not pd.api.types.is_numeric_dtype(df_filtrado['valor']):
        return "Dado Divergente"

    # Verifica se algum valor é maior que zero
    if (df_filtrado['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"
