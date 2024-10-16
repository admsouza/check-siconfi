import requests
import pandas as pd
from ..urls import API_DCA
from ...apis.dca.d2_00003 import d2_3_deducoes_fundeb


API_URL = API_DCA

def get_dca_i_c(id_ente, an_exercicio):
    """
    Faz a chamada à API e retorna os dados em um DataFrame.
    """
    url = f"{API_URL}?an_exercicio={an_exercicio}&id_ente={id_ente}&no_anexo=DCA-Anexo I-C"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('items', [])
        if data:
            return pd.DataFrame(data)  # Retorna os dados como um DataFrame
        else:
            return pd.DataFrame()  # Retorna um DataFrame vazio se não houver dados
    else:
        return pd.DataFrame()  # Retorna um DataFrame vazio se a API falhar

def main(id_ente, an_exercicio):
    """
    Faz a chamada à API uma única vez e processa os dados para VPD e VPA.
    """
    # Faz a chamada à API uma única vez
    df = get_dca_i_c(id_ente, an_exercicio)
    
    # Processa os dados para VPD e VPA usando o mesmo DataFrame
    deducoes_fundeb = d2_3_deducoes_fundeb(df)



    return deducoes_fundeb
