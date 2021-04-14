from flask_restful import Resource
from flask import request

COMPRAS = {
    1: {'Nombre': 'Compra 1'},
    2: {'Nombre': 'Compra 2'},
}

class Compras(Resource):
    def get(self):
        return COMPRAS

    def post(self):
        cliente = request.get_json()
        id = int(max(COMPRAS.keys())) + 1
        COMPRAS[id] = cliente
        return COMPRAS[id], 201


class Compra(Resource):
    def get(self, id):
        if int(id) in COMPRAS:
            return COMPRAS[int(id)]
        return '', 404

    def put(self, id):
        if int(id) in COMPRAS:
            compra = COMPRAS[int(id)]
            del COMPRAS[int(id)]
            compra2 = request.get_json()
            COMPRAS[id] = compra2
            return compra2, 201
        return '', 404

    def delete(self, id):
        if int(id) in COMPRAS:
            del COMPRAS[int(id)]
            return '', 204
        return '', 404
