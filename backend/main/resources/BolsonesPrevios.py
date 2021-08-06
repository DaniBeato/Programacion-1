from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels
from datetime import datetime, timedelta
from main.auth.decoradores import admin_required, verificacion_token_revocado


fecha_vencimiento = datetime.today() - timedelta(days=7)

class BolsonesPrevios(Resource):
    @admin_required
    @verificacion_token_revocado
    def get(self):
        bolsones_previos = db.session.query(BolsonesModels).filter(BolsonesModels.fecha <= fecha_vencimiento).all()
        return jsonify({'Bolsones Previos': [bolson_previo.hacia_json() for bolson_previo in bolsones_previos]})


class BolsonPrevio(Resource):
    @admin_required
    @verificacion_token_revocado
    def get(self, id):
        bolson_previo = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_previo.fecha <= fecha_vencimiento:
            return bolson_previo.hacia_json()
        else:
            return 'Este bolsón no ha caducado'


