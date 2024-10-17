import logging
from flask import Flask
from app.routes.home import home_bp
from app.routes.card_dimension import card_dimension_bp
from app.routes.dimensionii import dimensionii_bp
from app.routes.dimensioniii import dimensioniii_bp
from app.routes.dimensioniv import dimensioniv_bp
from dotenv import load_dotenv
import os

def create_app():

    load_dotenv()

    app = Flask(__name__)

    # Defina uma chave secreta para a aplicação
    app.secret_key = os.getenv('SECRET_KEY')

    # Configuração de logging para imprimir todas as mensagens no terminal
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Registrar os blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(card_dimension_bp)
    app.register_blueprint(dimensionii_bp)
    app.register_blueprint(dimensioniii_bp)
    app.register_blueprint(dimensioniv_bp)

    return app
