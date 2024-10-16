import requests
import pandas as pd
from ..urls import API_DCA

API_URL = API_DCA

def get_dca_i_hi(id_ente, an_exercicio):
    """
    Faz a chamada à API e retorna os dados em um DataFrame.
    """
    url = f"{API_URL}?an_exercicio={an_exercicio}&id_ente={id_ente}&no_anexo=DCA-Anexo I-HI"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('items', [])
        if data:
            return pd.DataFrame(data)  # Retorna os dados como um DataFrame
        else:
            return pd.DataFrame()  # Retorna um DataFrame vazio se não houver dados
    else:
        return pd.DataFrame()  # Retorna um DataFrame vazio se a API falhar