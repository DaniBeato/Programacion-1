from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels
from datetime import  datetime, timedelta

fecha_vencimiento = datetime.today() - timedelta(days=7)

class BolsonesVenta(Resource):
    def get(self):
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        bolsones_venta = db.session.query(BolsonesModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    bolsones_venta = bolsones_venta.filter(BolsonesModels.nombre == valor)
        bolsones_venta = bolsones_venta.filter(BolsonesModels.fecha >= fecha_vencimiento).filter(BolsonesModels.estado == True)
        bolsones_venta = bolsones_venta.order_by((BolsonesModels.fecha).desc())
        bolsones_venta = bolsones_venta.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Bolsones Venta': [bolson_venta.hacia_json() for bolson_venta in bolsones_venta.items],
                        'Cantidad total de bolsones en venta': bolsones_venta.total,
                        'Cantidad de páginas': bolsones_venta.pages,
                        'Página actual': pagina
                        })



class BolsonVenta(Resource):
    def get(self, id):
        bolson_venta = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_venta.fecha >= fecha_vencimiento and bolson_venta.estado == True:
            return bolson_venta.hacia_json()
        else:
            return 'Este bolsón no está a la venta', 400



