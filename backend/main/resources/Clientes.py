from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClientesModels



class Clientes(Resource):
    def get(self):
        clientes = db.session.query(ClientesModels).all()
        return jsonify([cliente.hacia_json() for cliente in clientes])



    def post(self):
        cliente = ClientesModels.desde_json(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente.hacia_json(), 201


class Cliente(Resource):
    def get(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        return cliente.hacia_json()

    def put(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(cliente, clave, valor)
        db.session.add(cliente)
        db.session.commit()
        return cliente.hacia_json()

    def delete(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204

