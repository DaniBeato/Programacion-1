from flask_restful import Resource
from flask import request

BOLSONES_PENDIENTES = {
    1: {'Nombre': 'Bolson pendiente1'},
    2: {'Nombre': 'Bolson pendiente2'},
}


class BolsonesPendientes(Resource):
    def get(self):
        return BOLSONES_PENDIENTES

    def post(self):
        bolson_pendiente = request.get_json()
        id = int(max(BOLSONES_PENDIENTES.keys())) + 1
        BOLSONES_PENDIENTES[id] = bolson_pendiente
        return BOLSONES_PENDIENTES[id], 201



class BolsonPendiente(Resource):
    def get(self, id):
        if int(id) in BOLSONES_PENDIENTES:
            return BOLSONES_PENDIENTES[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in BOLSONES_PENDIENTES:
            del BOLSONES_PENDIENTES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in BOLSONES_PENDIENTES:
            bolson = BOLSONES_PENDIENTES[int(id)]
            del BOLSONES_PENDIENTES[int(id)]
            bolson2 = request.get_json()
            BOLSONES_PENDIENTES[id] = bolson2
            return bolson2, 201
        return '', 404