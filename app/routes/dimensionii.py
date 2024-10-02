from flask import Blueprint, render_template

dimensionii_bp = Blueprint('dimensionii_bp', __name__)

@dimensionii_bp.route('/dimension_ii')
def dimension_ii():
    return render_template('dimension_ii.html')
