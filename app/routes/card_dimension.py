from flask import Blueprint, render_template

# Criação do blueprint para card_dimension
card_dimension_bp = Blueprint('card_dimension_bp', __name__)

@card_dimension_bp.route('/card_dimension')
def card_dimension():
    return render_template('card_dimension.html')  # Renderiza o template
