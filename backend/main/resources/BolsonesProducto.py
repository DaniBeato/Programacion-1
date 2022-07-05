from .. import db
from flask_restful import Resource
from main.models import Productos_BolsonesModels
from main.auth.decoradores import admin_required, verificacion_token_revocado
from flask import request, jsonify

class BolsonesProductos(Resource):
    @admin_required
    @verificacion_token_revocado
    def get(self):
        filtros = request.data
        bolsones_productos = db.session.query(Productos_BolsonesModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'bolson_ID':
                    bolsones_productos = bolsones_productos.filter(Productos_BolsonesModels.bolson_ID == valor)
        return jsonify({'Bolsones Productos': [bolson.hacia_json() for bolson in bolsones_productos]})

    @admin_required
    @verificacion_token_revocado
    def post(self):
        producto_bolson = Productos_BolsonesModels.desde_json(request.get_json())
        db.session.add(producto_bolson)
        db.session.commit()
        return producto_bolson.hacia_json(), 204

class BolsonProducto(Resource):
    @admin_required
    @verificacion_token_revocado
    def put(self, id):
        producto_bolson = db.session.query(Productos_BolsonesModels).filter(Productos_BolsonesModels.bolson_ID == id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(producto_bolson, clave, valor)
        db.session.add(producto_bolson)
        db.session.commit()
        return producto_bolson.hacia_json(), 204
