from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels




class BolsonesPendientes(Resource):
    def get(self):
        bolsones_pendientes = db.session.query(BolsonesModels).all()
        return ([bolson_pendiente.hacia_json() for bolson_pendiente in bolsones_pendientes])

    def post(self):
        bolson_pendiente = BolsonesModels.desde_json(request.get_json())
        db.session.add(bolson_pendiente)
        db.session.commit()
        return bolson_pendiente.hacia_json(), 201


class BolsonPendiente(Resource):
    def get(self, id):
        bolson_pendiente = db.session.query(BolsonesModels).get_or_404(id)
        return bolson_pendiente.hacia_json()

    def delete(self, id):
        bolson_pendiente = db.session.query(BolsonesModels).get_or_404(id)
        db.session.delete(bolson_pendiente)
        db.session.commit()
        return '', 204

    def put(self, id):
        bolson_pendiente = db.session.query(BolsonesModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(bolson_pendiente, clave, valor)
        db.session.add(bolson_pendiente)
        db.session.commit()
        return bolson_pendiente.hacia_json(), 201



