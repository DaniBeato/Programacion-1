from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels
from datetime import  datetime, timedelta

fecha_vencimiento = datetime.today() - timedelta(days=7)

class BolsonesVenta(Resource):
    def get(self):
        bolsones_venta = db.session.query(BolsonesModels).filter(BolsonesModels.fecha >= fecha_vencimiento).filter(BolsonesModels.estado == True).all()
        return jsonify({'Bolsones en Venta': [bolson_venta.hacia_json() for bolson_venta in bolsones_venta]})


class BolsonVenta(Resource):
    def get(self, id):
        bolson_venta = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_venta.fecha >= fecha_vencimiento and bolson_venta.estado == True:
            return bolson_venta.hacia_json()
        else:
            return 'Este bolsón no está a la venta'



