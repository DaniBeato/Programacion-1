from flask_restful import Resource
from flask import request

CLIENTES = {
    1: {'Nombre': 'Daniel'},
    2: {'Nombre': 'Jesús'},
       }

class Clientes(Resource):
    def get(self):
        return CLIENTES

    def post(self):
        cliente = request.get_json()
        id = int(max(CLIENTES.keys())) + 1
        CLIENTES[id] = cliente
        return CLIENTES[id], 201


class Cliente(Resource):
    def get(self, id):
        if int(id) in CLIENTES:
            return CLIENTES[int(id)]
        return '', 404

    def put(self, id):
        if int(id) in Clientes:
            cliente = CLIENTES[int(id)]
            del CLIENTES[int(id)]
            cliente2 = request.get_json()
            CLIENTES[id] = cliente2
            return cliente2, 201
        return '', 404

    def delete(self, id):
        if int(id) in CLIENTES:
            del CLIENTES[int(id)]
            return '', 204
        return '', 404




