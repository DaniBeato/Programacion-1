from flask_restful import Resource
from main.models import Productos_BolsonesModels, BolsonesModels
from main.auth.decoradores import admin_required, verificacion_token_revocado
from flask import request

class ProductosBolsones(Resource):

    @admin_required
    @verificacion_token_revocado
    def post(self):
        producto_bolson = Productos_BolsonesModels.desde_json(request.get_json())
        db.session.add(producto_bolson)
        db.session.commit()
        return producto_bolson.hacia_json(), 204

class ProductoBolson(Resource):
    @admin_required
    @verificacion_token_revocado
    def put(self, id1, id2):
        producto_bolson = db.session.query(Productos_BolsonesModels).filter(Productos_BolsonesModels.producto_ID == id1).filter(Productos_BolsonesModels.bolson_ID == id2)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(producto_bolson, clave, valor)
        db.session.add(producto_bolson)
        db.session.commit()
        return producto_bolson.hacia_json(), 204
