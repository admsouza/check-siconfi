from flask import Flask
from app.routes.home import home_bp
from app.routes.card_dimension import card_dimension_bp
from app.routes.dimensionii import dimensionii_bp
from app.routes.dimensioniii import dimensioniii_bp
from app.routes.dimensioniv import dimensioniv_bp

def create_app():
    app = Flask(__name__)

    # Registrar os blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(card_dimension_bp)
    app.register_blueprint(dimensionii_bp)
    app.register_blueprint(dimensioniii_bp)
    app.register_blueprint(dimensioniv_bp)

    return app
