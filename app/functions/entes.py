import requests

# Função auxiliar para obter os entes, ufs e cidades
def get_ufs_cidades():
    response = requests.get('https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes')
    data = response.json()['items']

    # Filtrar estados e cidades, ignorando valores None e ordenar alfabeticamente
    ufs = sorted(list(set(item['uf'] for item in data if item['uf'] is not None)))
    
    # Garantir que o campo correto seja utilizado e que ele exista
    cidades = {
        uf: sorted(
            [item for item in data if item['uf'] == uf and 'nome_ente' in item], 
            key=lambda x: x['nome_ente']
        ) for uf in ufs
    }
    
    return ufs, cidades
