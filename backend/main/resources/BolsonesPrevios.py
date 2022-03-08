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
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        bolsones_previos = db.session.query(BolsonesModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    bolsones_previos = bolsones_previos.filter(BolsonesModels.nombre == valor)
                if clave == 'estado':
                    bolsones_previos = bolsones_previos.filter(BolsonesModels.estado == valor)
                if clave == 'desde':
                    bolsones_previos = bolsones_previos.filter(BolsonesModels.fecha >= datetime.strptime(valor, '%d/%m/%Y'))
                if clave == 'hasta':
                    bolsones_previos = bolsones_previos.filter(BolsonesModels.fecha <= datetime.strptime(valor, '%d/%m/%Y'))
        bolsones_previos = bolsones_previos.filter(BolsonesModels.fecha <= fecha_vencimiento)
        bolsones_previos = bolsones_previos.order_by(BolsonesModels.fecha)
        bolsones_previos = bolsones_previos.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Bolsones Previos': [bolson_previo.hacia_json() for bolson_previo in bolsones_previos.items],
                        'Cantidad total de bolsones previos': bolsones_previos.total,
                        'Cantidad de páginas': bolsones_previos.pages,
                        'Página actual': pagina
                        })


class BolsonPrevio(Resource):
    @admin_required
    @verificacion_token_revocado
    def get(self, id):
        bolson_previo = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_previo.fecha <= fecha_vencimiento:
            return bolson_previo.hacia_json()
        else:
            return 'Este bolsón no ha caducado', 400


