from flask import Blueprint, render_template

dimensioniv_bp = Blueprint('dimensioniv_bp', __name__)

@dimensioniv_bp.route('/dimension_iv')
def dimension_iv():
    return render_template('dimension_iv.html')
