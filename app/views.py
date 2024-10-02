from flask import Blueprint, render_template, request, jsonify, redirect, url_for, current_app
import os
from .functions.entes import get_ufs_cidades
from .functions.periodo import get_anos_meses
import requests

# Criação do blueprint
main = Blueprint('main', __name__)

# Rota que renderiza a página inicial (home)
@main.route('/')
def home():
    # Obter os dados iniciais de UFs, cidades, anos e meses
    ufs, cidades = get_ufs_cidades()
    anos, meses = get_anos_meses()
    
    return render_template('home.html', ufs=ufs, anos=anos, meses=meses, cidades=cidades)

# Rota que recebe os parâmetros do formulário e redireciona para a página de dimensões
@main.route('/enviar_parans', methods=['POST'])
def enviar_parans():
    # Captura os parâmetros enviados pelo formulário
    id_ente = request.form['id_ente']
    an_referencia = request.form['an_referencia']
    me_referencia = request.form['me_referencia']

    # Você pode adicionar a lógica para processar os dados aqui, se necessário
    
    # Redirecionar para a página de dimensões após enviar os parâmetros
    return redirect(url_for('main.main_dimensoes'))

# Rota para renderizar a página main_dimensoes
@main.route('/main_dimensoes')
def main_dimensoes():
    # Renderizar o template main_dimensoes.html
    return render_template('main_dimensoes.html')

# Rota para Dimensão II
@main.route('/dimensao_ii')
def dimensao_ii():
    return render_template('dimensao_ii.html')

# Rota para Dimensão III
@main.route('/dimensao_iii')
def dimensao_iii():
    # Código de depuração para verificar o caminho do template
    print("Template path:", os.path.join(current_app.root_path, 'templates', 'dimensao_iii.html'))
    
    return render_template('dimensao_iii.html')

# Rota para Dimensão IV
@main.route('/dimensao_iv')
def dimensao_iv():
    return render_template('dimensao_iv.html')

# Rota que retorna as cidades baseadas na UF
@main.route('/get_cidades/<uf>', methods=['GET'])
def get_cidades(uf):
    response = requests.get('https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes')
    data = response.json()['items']
    
    cidades = [item for item in data if item['uf'] == uf]
    return jsonify(cidades)
