from flask import Blueprint, render_template, request, jsonify, redirect, url_for, current_app
import os
from .functions.entes import get_ufs_cidades
from .functions.periodo import get_anos
import requests

# Criação do blueprint
main = Blueprint('main', __name__)

# Rota que renderiza a página inicial (home)
@main.route('/')
def home():
    # Obter os dados iniciais de UFs, cidades, anos e meses
    ufs, cidades = get_ufs_cidades()
    anos= get_anos()
    
    return render_template('home.html', ufs=ufs, anos=anos, cidades=cidades)

# Rota que recebe os parâmetros do formulário e redireciona para a página de dimensões
@main.route('/enviar_parans', methods=['POST'])
def enviar_parans():
    # Captura os parâmetros enviados pelo formulário
    id_ente = request.form['id_ente']
    an_referencia = request.form['an_referencia']

    # Você pode adicionar a lógica para processar os dados aqui, se necessário
    
    # Redirecionar para a página de dimensões após enviar os parâmetros
    return redirect(url_for('main.card_dimension'))

# Rota para renderizar a página main_dimensoes
@main.route('/card_dimension')
def card_dimension():
    # Renderizar o template main_dimensoes.html
    return render_template('card_dimension.html')

# Rota para Dimensão II
@main.route('/dimension_ii')
def dimension_ii():
    return render_template('dimension_ii.html')

# Rota para Dimensão III
@main.route('/dimension_iii')
def dimension_iii():
    # Código de depuração para verificar o caminho do template
    print("Template path:", os.path.join(current_app.root_path, 'templates', 'dimension_iii.html'))
    
    return render_template('dimension_iii.html')

# Rota para Dimensão IV
@main.route('/dimension_iv')
def dimension_iv():
    return render_template('dimension_iv.html')

# Rota que retorna as cidades baseadas na UF
@main.route('/get_cidades/<uf>', methods=['GET'])
def get_cidades(uf):
    response = requests.get('https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes')
    data = response.json()['items']
    
    cidades = [item for item in data if item['uf'] == uf]
    return jsonify(cidades)
