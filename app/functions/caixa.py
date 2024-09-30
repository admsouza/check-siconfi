import pandas as pd

def process_data(data):
    df = pd.DataFrame(data)

    # Limpar e preparar os dados
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df['data_referencia'] = pd.to_datetime(df['data_referencia'], errors='coerce')

    # Filtrar os dados para natureza C
    filtered_C = df[
        (df['conta_contabil'].str.contains("11111")) & 
        (df['natureza_conta'] == "C") & 
        (df['tipo_valor'] == "ending_balance") 
     
    ]

    # Filtrar os dados para natureza D
    filtered_D = df[
        (df['conta_contabil'].str.contains("11111")) & 
        (df['natureza_conta'] == "D") & 
        (df['tipo_valor'] == "ending_balance") 
      
    ]

    # Calcular os totais somados
    total_C = filtered_C['valor'].sum()
    total_D = filtered_D['valor'].sum()

    # Subtrair o total de C do total de D
    resultado = total_D - total_C

    return resultado
