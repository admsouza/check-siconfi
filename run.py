from app import create_app
import os

app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    # Configure para escutar em qualquer host e utilize a porta definida pelo serviço de deploy.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)