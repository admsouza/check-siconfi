import math

# percentual_calculator.py

def calcular_percentual(results):
    """
    Calcula o percentual de 'Dado Consistente' e 'Dado Divergente' em um dicionário de resultados.
    
    :param results: Dicionário com os resultados das funções que retornam 'Dado Consistente' ou 'Dado Divergente'.
    :return: Um dicionário com os percentuais de 'Dado Consistente' e 'Dado Divergente'.
    """
    consistente_count = 0
    divergente_count = 0
    total_items = 0

    # Iterando pelos resultados e contando as ocorrências
    for key, result in results.items():
        total_items += 1
        if result == 'Dado Consistente':
            consistente_count += 1
        elif result == 'Dado Divergente':
            divergente_count += 1

    # Evitar divisão por zero
    if total_items == 0:
        return {"Percentual Consistente": 0, "Percentual Divergente": 0, "Total Percentual": 100}

    # Calculando os percentuais
    percentual_consistente = (consistente_count / total_items) * 100
    percentual_divergente = (divergente_count / total_items) * 100

 
    
    # Ajustar o percentual consistente para garantir que a soma seja 100
    percentual_consistente = 100 - percentual_divergente

    # Retornar os percentuais e o total como 100%
    return {
        "Percentual Consistente": percentual_consistente,
        "Percentual Divergente": percentual_divergente,
        "Total Percentual": 100
    }
