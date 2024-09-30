import pandas as pd

def movextra_data(data):
    df = pd.DataFrame(data)

    # Limpar e preparar os dados
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df['data_referencia'] = pd.to_datetime(df['data_referencia'], errors='coerce')

    # Verificar se há valores não numéricos em 'valor' ou datas inválidas
    print("Valores antes da filtragem:", df['valor'].head())
    print("Datas antes da filtragem:", df['data_referencia'].head())

    # Remover valores nulos que possam causar problemas
    df = df.dropna(subset=['valor', 'data_referencia'])

    # Verificar como o DataFrame está após remover NaNs
    print("DataFrame após remover NaNs:", df.head())

    # Filtrar os dados para natureza C
    filtered = df[
        (df['conta_contabil'].str.contains("1138", na=False)) & 
        (df['natureza_conta'] == "D") &
        (df['tipo_valor'] == "period_change")
       
    ]

    # Verificar o DataFrame filtrado
    print("DataFrame filtrado:", filtered.head())

    # Somar os valores da coluna 'valor' no DataFrame filtrado
    total = filtered['valor'].sum()

    # Verificar o total calculado
    print("Total calculado:", total)

    resultadoextra = total

    return resultadoextra
