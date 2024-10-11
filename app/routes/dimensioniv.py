import logging
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..utils.format_currency import format_currency  # Importando a função de formatação de moeda
from ..apis.msc.apicaixa import get_api_caixa  # Importando a função para obter dados da API

# Criação do blueprint para o dimensioniv
dimensioniv_bp = Blueprint('dimensioniv_bp', __name__)

@dimensioniv_bp.route('/dimensioniv', methods=['GET'])
def dimensioniv():
    id_ente = request.args.get('id_ente')
    an_referencia = request.args.get('an_referencia')

    # logging.info(f"Carregando dados para Dimensão IV: id_ente={id_ente}, an_referencia={an_referencia}")

    if not id_ente or not an_referencia:
        flash("Parâmetros 'id_ente' e 'an_referencia' são necessários.", "warning")
        return redirect(url_for('home_bp.home'))

    # Obtendo dados da API
    resultado = get_api_caixa(id_ente, an_referencia)

    if resultado is None:
        flash("Resultado não encontrado. Por favor, tente novamente com outros parâmetros.", "warning")
        return redirect(url_for('home_bp.home'))

    # Formata o resultado
    resultado_formatado = format_currency(resultado)

    return render_template('dimension_iv.html', resultado=resultado_formatado)
