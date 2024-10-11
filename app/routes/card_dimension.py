from flask import Blueprint, render_template, request, redirect, url_for, flash

# Criação do blueprint para card_dimension
card_dimension_bp = Blueprint('card_dimension_bp', __name__)

@card_dimension_bp.route('/card_dimension', methods=['GET'])
def card_dimension():
    """
    Rota para a página 'card_dimension'.
    Carrega as opções de dimensões.
    """
    return render_template('card_dimension.html')  # Renderiza o template que contém os links para as dimensões
