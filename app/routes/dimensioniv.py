import logging
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..utils.format_currency import format_currency  # Importando a função de formatação de moeda


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

    return render_template('dimension_iv.html')
