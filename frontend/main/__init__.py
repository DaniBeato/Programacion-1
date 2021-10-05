import os
from flask import Flask
from dotenv import load_dotenv



from main.routes import bolson
from main.routes import main
from main.routes import usuario

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.register_blueprint(routes.main.main)
    app.register_blueprint(routes.bolson.bolson)
    app.register_blueprint(routes.usuario.usuario)
    return app