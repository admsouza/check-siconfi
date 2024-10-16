from .dca_anexo_i_hi import get_dca_i_hi

def vpa_fundeb_principal(id_ente, an_exercicio):  
    """
    Chama os dados da API e aplica o filtro específico para VPA.
    """
    df = get_dca_i_hi(id_ente, an_exercicio)  # Chama a função do módulo
    
    # Processa os dados diretamente dentro da função
    if df.empty:
        return "Dado Divergente"  # Retorna "Dado Divergente" se o DataFrame estiver vazio

    # Verifica se a coluna 'conta' existe no DataFrame
    if 'conta' not in df.columns:
        return "Dado Divergente"  # Retorna "Dado Divergente" se a coluna não existir

    # Filtra as linhas onde a coluna 'conta' contém o filtro específico
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
