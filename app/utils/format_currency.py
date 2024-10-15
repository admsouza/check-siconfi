def format_currency(value):
    """Formata um valor numérico como moeda brasileira."""
    return f'R$ {value:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')






# import locale

# # Configuração da localidade para formato em reais
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Para Linux e MacOS
# # locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')  # Para Windows

# def format_currency(value):
#     """
#     Formata um valor numérico como moeda em reais (R$).
#     """
#     try:
#         value_float = float(value)
#         return locale.currency(value_float, symbol=True, grouping=True)
#     except (ValueError, TypeError):
#         return "Valor INVÁLIDO"
