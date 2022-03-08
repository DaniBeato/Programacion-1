from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductosModels
from main.auth.decoradores import admin_required, proveedor_required, admin_or_proveedor_required, verificacion_token_revocado


class Productos(Resource):
    #@admin_or_proveedor_required
    @verificacion_token_revocado
    def get(self):
        pagina = 1
        cantidad_elementos = 30
        filtros = request.data
        productos = db.session.query(ProductosModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    productos = productos.filter(ProductosModels.nombre == valor)
        productos = productos.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Productos': [producto.hacia_json() for producto in productos.items],
                        'Cantidad total de productos': productos.total,
                        'Cantidad de páginas': productos.pages,
                        'Página actual': pagina
                        })


    @admin_or_proveedor_required
    @verificacion_token_revocado
    def post(self):
        producto = ProductosModels.desde_json(request.get_json())
        db.session.add(producto)
        db.session.commit()
        return producto.hacia_json(), 201


class Producto(Resource):
    def get(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        return producto.hacia_json(), 201

    @admin_or_proveedor_required
    @verificacion_token_revocado
    def put(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(producto, clave, valor)
        db.session.add(producto)
        db.session.commit()
        return producto.hacia_json(), 201

    @admin_or_proveedor_required
    @verificacion_token_revocado
    def delete(self, id):
        producto = db.session.query(ProductosModels).get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return '', 201
