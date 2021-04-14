from flask_restful import Resource
from flask import request

BOLSONES_PREVIOS = {
    1: {'Nombre': 'Bolsón Pendiente 1'},
    2: {'Nombre': 'Bolsón Pendiente 2'},
}


class BolsonesPrevios(Resource):
    def get(self):
        return BOLSONES_PREVIOS


class BolsonPrevio(Resource):
    def get(self, id):
        if int(id) in BOLSONES_PREVIOS:
            return  BOLSONES_PREVIOS[int(id)]
        return '', 404