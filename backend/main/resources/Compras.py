from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ComprasModels




class Compras(Resource):
    def get(self):
        compras = db.session.query(ComprasModels).all()
        return jsonify([compra.hacia_json() for compra in compras])

    def post(self):
        compra = ComprasModels.desde_json(request.get_json())
        db.session.add(compra)
        db.session.commit()
        return compra.hacia_json(), 201


class Compra(Resource):
    def get(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        return compra.hacia_json()


    def put(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(compra, clave, valor)
        db.session.add(compra)
        db.session.commit()
        return compra.hacia_json(), 201


    def delete(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        db.session.delete(compra)
        db.session.commit()
        return '', 204
