from flask import Blueprint, render_template, current_app
import os

dimensioniii_bp = Blueprint('dimensioniii_bp', __name__)

@dimensioniii_bp.route('/dimension_iii')
def dimension_iii():
    print("Template path:", os.path.join(current_app.root_path, 'templates', 'dimension_iii.html'))
    return render_template('dimension_iii.html')
