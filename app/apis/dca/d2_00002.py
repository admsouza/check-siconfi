import pandas as pd

# DCA-Anexo I-HI

def d2_2_vpd_fundeb_principal(df):  
    """
    Processa o DataFrame filtrando os dados específicos para VPD.
    """
    if df.empty:
        return "Dado Divergente"

    if 'conta' not in df.columns:
        return "Dado Divergente"

    filtered_df = df[df['conta'].str.contains('3.5.2.2.4', na=False)]

    if filtered_df.empty:
        return "Dado Divergente"

    if not pd.api.types.is_numeric_dtype(filtered_df['valor']):
        return "Dado Divergente"


    if (filtered_df['valor'] > 0).any():
        return "Dado Consistente"
    else:
        return "Dado Divergente"
