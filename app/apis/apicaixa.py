
import requests

API_URL = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/msc_patrimonial'

def get_api_data(id_ente, an_referencia, me_referencia):
    params = {
        'id_ente': id_ente,
        'an_referencia': an_referencia,
        'me_referencia': me_referencia,
        'co_tipo_matriz': 'MSCC',
        'classe_conta': 1,
        'id_tv': 'ending_balance'
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()['items']
    else:
        return []
