from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuariosModels


class Usuarios(Resource):
    def get(self):
        usuarios = db.session.query(UsuariosModels).all()
        return jsonify([usuario.hacia_json() for usuario in usuarios])


class Usuario(Resource):
    def get(self, id):
        usuario = db.session.query(UsuariosModels).get_or_404(id)
        return usuario.hacia_json()