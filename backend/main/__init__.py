import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources
api = Api()



def create_app():
    app = Flask(__name__)
    load_dotenv()
    api.add_resource(resources.ProfessorsResource, '/professors')
    api.add_resource(resources.ProfessorResource, '/professor/<id>')
    api.init_app(app)
    return app