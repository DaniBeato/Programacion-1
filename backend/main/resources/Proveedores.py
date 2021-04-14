from flask_restful import Resource
from flask import request

PROVEEDORES = {
    1: {'Nombre': 'José'},
    2: {'Nombre': 'Gabriel'},
}

class Proveedores(Resource):
    def get(self):
        return PROVEEDORES

    def post(self):
        proveedor = request.get_json()
        id = int(max(PROVEEDORES.keys())) + 1
        PROVEEDORES[id] = proveedor
        return PROVEEDORES[id], 201


class Proveedor(Resource):
    def get(self, id):
        if int(id) in PROVEEDORES:
            return PROVEEDORES[int(id)]
        return '', 404

    def put(self, id):
        if int(id) in PROVEEDORES:
            proveedor = PROVEEDORES[int(id)]
            del PROVEEDORES[int(id)]
            proveedor2 = request.get_json()
            PROVEEDORES[id] = proveedor2
            return proveedor2, 201
        return '', 404

    def delete(self, id):
        if int(id) in PROVEEDORES:
            del PROVEEDORES[int(id)]
            return '', 204
        return '', 404

