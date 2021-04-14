from flask_restful import Resource
from flask import request

PRODUCTOS = {
    1: {'Nombre': 'Tomate'},
    2: {'Nombre': 'Papa'},
}

class Productos(Resource):
    def get(self):
        return PRODUCTOS

    def post(self):
        producto = request.get_json()
        id = int(max(PRODUCTOS.keys())) + 1
        PRODUCTOS[id] = producto
        return PRODUCTOS[id], 201



class Producto(Resource):
    def get(self, id):
        if int(id) in PRODUCTOS:
            return PRODUCTOS[int(id)]
        return '', 404

    def put(self, id):
        if int(id) in PRODUCTOS:
            producto = PRODUCTOS[int(id)]
            del PRODUCTOS[int(id)]
            producto2 = request.get_json()
            PRODUCTOS[id] = producto2
            return producto2, 201
        return '', 404

    def delete(self, id):
        if int(id) in PRODUCTOS:
            del PRODUCTOS[int(id)]
            return '', 204
        return '', 404
