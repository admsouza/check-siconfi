import requests
import pandas as pd
from ...urls import API_DCA
from ..d2_00005 import d2_5_desp_patronal_empenhada
from ..d2_00006 import d2_6_desp_pessoal_empenhada
from ..d2_00007 import d2_7_desp_custeio_empenhada


API_URL = API_DCA

def get_dca_i_d(id_ente, an_exercicio):
    """
    Faz a chamada à API e retorna os dados em um DataFrame.
    """
    url = f"{API_URL}?an_exercicio={an_exercicio}&id_ente={id_ente}&no_anexo=DCA-Anexo I-D"
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
    df = get_dca_i_d(id_ente, an_exercicio)
    
    # Processa os dados usando o mesmo DataFrame
    desp_patronal_empenhada = d2_5_desp_patronal_empenhada(df)
    desp_pessoal_empenhada = d2_6_desp_pessoal_empenhada(df)
    desp_custeio_empenhada = d2_7_desp_custeio_empenhada(df)



    return desp_patronal_empenhada, desp_pessoal_empenhada, desp_custeio_empenhada
