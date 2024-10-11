def format_currency(value):
    # Formata o valor para moeda brasileira
    return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')