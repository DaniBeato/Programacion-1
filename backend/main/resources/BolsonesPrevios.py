from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels
from datetime import datetime, timedelta

fecha_vencimiento = datetime.today() - timedelta(days=7)

class BolsonesPrevios(Resource):
    def get(self):
        bolsones_previos = db.session.query(BolsonesModels).filter(BolsonesModels.fecha <= fecha_vencimiento).all()
        return jsonify({'Bolsones Previos': [bolson_previo.hacia_json() for bolson_previo in bolsones_previos]})


class BolsonPrevio(Resource):
    def get(self, id):
        bolson_previo = db.session.query(BolsonesModels).get_or_404(id)
        return bolson_previo.hacia_json()


