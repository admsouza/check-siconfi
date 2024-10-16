def d2_3_deducoes_fundeb(df):  
   
    if df.empty:
        return "Dado Divergente"

    # Verifica se a coluna 'conta' existe no DataFrame
    if 'coluna' not in df.columns:
        return "Dado Divergente"  # Retorna "Dado Divergente" se a coluna não existir

    # Filtra as linhas onde a coluna 'conta' contém 'Deduções - FUNDEB'
    filtered_df = df[df['coluna'].str.contains('Deduções - FUNDEB', na=False)]

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
