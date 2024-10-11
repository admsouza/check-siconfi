import logging
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..apis.msc.apicaixa import get_api_caixa, dado_final  # Importando a função para obter dados da API

# Criação do blueprint para o dimensionii
dimensionii_bp = Blueprint('dimensionii_bp', __name__)

@dimensionii_bp.route('/dimensionii', methods=['GET'])
def dimensionii():
    id_ente = request.args.get('id_ente')
    an_referencia = request.args.get('an_referencia')

    # logging.info(f"Carregando dados para Dimensão II: id_ente={id_ente}, an_referencia={an_referencia}")

    if not id_ente or not an_referencia:
        # logging.error("Parâmetros ausentes.")
        flash("Parâmetros 'id_ente' e 'an_referencia' são necessários.", "warning")
        return redirect(url_for('home_bp.home'))

    # Obtendo dados da API
    resultado = get_api_caixa(id_ente, an_referencia)

    if resultado is None:
        # logging.warning("Nenhum resultado encontrado, redirecionando para home.")
        flash("Resultado não encontrado. Por favor, tente novamente com outros parâmetros.", "warning")
        return redirect(url_for('home_bp.home'))

    # Formata o resultado
    

    # Chama a função dado_final para obter o status dos dados
    status_dados_d1 = dado_final(resultado)

    # logging.info("Renderizando o template dimension_ii.html com o resultado formatado.")
    return render_template('dimension_ii.html', status= status_dados_d1)
