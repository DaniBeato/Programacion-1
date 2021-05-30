from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels
from datetime import  datetime, timedelta

fecha_vencimiento = datetime.today() - timedelta(days=7)

class BolsonesVenta(Resource):
    def get(self):
        bolsones_venta = db.session.query(BolsonesModels).filter(BolsonesModels.fecha >= fecha_vencimiento).all()
        return jsonify({'Bolsones en Venta': [bolson_venta.hacia_json() for bolson_venta in bolsones_venta]})


class BolsonVenta(Resource):
    def get(self, id):
        bolson_venta = db.sesion.query(BolsonesModels).get_or_404(id)
        return bolson_venta.hacia_json()



