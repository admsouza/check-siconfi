from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from ..functions.entes import get_ufs_cidades
from ..functions.period import get_anos
import requests

# Criação do blueprint para o home
home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    ufs, cidades = get_ufs_cidades()
    anos = get_anos()
    
    return render_template('home.html', ufs=ufs, anos=anos, cidades=cidades)

@home_bp.route('/enviar_parans', methods=['POST'])
def enviar_parans():
    id_ente = request.form['id_ente']
    an_referencia = request.form['an_referencia']
    
    # Aqui você pode adicionar lógica para processar os dados se necessário

    return redirect(url_for('home_bp.card_dimension'))  # Redireciona para card_dimension

@home_bp.route('/card_dimension')  # Rota para a página card_dimension
def card_dimension():
    # Aqui você pode passar dados para o template, se necessário
    return render_template('card_dimension.html')  # Renderiza o template

@home_bp.route('/get_cidades/<uf>', methods=['GET'])
def get_cidades(uf):
    response = requests.get('https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes')
    data = response.json()['items']
    
    cidades = [item for item in data if item['uf'] == uf]
    return jsonify(cidades)
