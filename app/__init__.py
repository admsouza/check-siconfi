from flask import Flask
from .views import main  # Importa o Blueprint

def create_app():
    app = Flask(__name__)
    
    # Registra o Blueprint
    app.register_blueprint(main)

    return app
