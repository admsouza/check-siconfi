from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
import logging
import requests  # Para fazer a requisição externa à API
from ..apis.msc.apicaixa import get_api_caixa
from ..utils.entes import get_ufs_cidades
from ..utils.period import get_anos

# Criação do blueprint para o home
home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    """
    Rota principal que carrega a página inicial.
    Obtém as UFs, cidades e anos para exibir no template.
    """
    ufs, cidades = get_ufs_cidades()
    anos = get_anos()
    return render_template('home.html', ufs=ufs, anos=anos, cidades=cidades)

@home_bp.route('/enviar_parans', methods=['POST'])
def enviar_parans():
    id_ente = request.form.get('id_ente')
    an_referencia = request.form.get('an_referencia')

    logging.info(f"Parâmetro id_ente: {id_ente}, an_referencia: {an_referencia}")

    if not id_ente or not an_referencia:
        logging.warning("Parâmetros inválidos, redirecionando para home.")
        flash("Por favor, forneça todos os parâmetros necessários.", "warning")
        return redirect(url_for('home_bp.home'))

    # Chamando a API para obter dados
    resultado = get_api_caixa(id_ente, an_referencia)  # Obtendo o resultado da API
    logging.info(f"Resultado obtido da API: {resultado}")

    if resultado is None:
        logging.warning("Nenhum resultado encontrado, redirecionando para home.")
        flash("Resultado não encontrado. Por favor, tente novamente com outros parâmetros.", "warning")
        return redirect(url_for('home_bp.home'))


    return redirect(url_for('card_dimension_bp.card_dimension', id_ente=id_ente, an_referencia=an_referencia))

@home_bp.route('/get_cidades/<uf>', methods=['GET'])
def get_cidades(uf):
    """
    Rota que retorna as cidades com base no estado (UF) selecionado.
    Faz uma requisição externa para obter os dados das cidades.
    """
    response = requests.get('https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes')
    
    if response.status_code == 200:
        data = response.json()['items']
        cidades = [item for item in data if item['uf'] == uf]
        return jsonify(cidades)
    else:
        return jsonify({"error": "Erro ao buscar cidades"}), 500
