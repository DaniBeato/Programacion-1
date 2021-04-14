from flask_restful import Resource
from flask import request

BOLSONES_VENTA = {
    1: {'Nombre': 'Bolsón Venta 1'},
    2: {'Nombre': 'Bolsón Venta 2'},
}


class BolsonesVenta(Resource):
    def get(self):
        return BOLSONES_VENTA


class BolsonVenta(Resource):
    def get(self, id):
        if int(id) in BOLSONES_VENTA:
            return BOLSONES_VENTA[int(id)]
        return '', 404
