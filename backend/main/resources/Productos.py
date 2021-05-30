from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductosModels


class Productos(Resource):
    def get(self):
        filtros = request.data
        productos = db.session.query(ProductosModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'proveedor_ID':
                    productos = productos.filter(ProductosModels.proveedor_ID == valor)
                if clave == 'nombre':
                    productos = productos.filter(ProductosModels.nombre == valor)
        productos = productos.all()
        return jsonify({'Productos': [producto.hacia_json() for producto in productos]})

    def post(self):
        producto = ProductosModels.desde_json(request.get_json())
        db.session.add(producto)
        db.session.commit()
        return producto.hacia_json(), 201


class Producto(Resource):
    def get(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        return producto.hacia_json()


    def put(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(producto, clave, valor)
        db.session.add(producto)
        db.session.commit()
        return producto.hacia_json(), 201


    def delete(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return '', 204
