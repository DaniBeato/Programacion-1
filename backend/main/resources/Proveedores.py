from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProveedoresModels



class Proveedores(Resource):
    def get(self):
        proveedores = db.session.query(ProveedoresModels).all()
        return jsonify([proveedor.hacia_json() for proveedor in proveedores])

    def post(self):
        proveedor = ProveedoresModels.desde_json(request.get_json())
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.hacia_json(), 201


class Proveedor(Resource):
    def get(self, id):
        proveedor = db.session.query(ProveedoresModels).get_or_404(id)
        return proveedor.hacia_json()

    def put(self, id):
        proveedor = db.session.query(ProveedoresModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(proveedor, clave, valor)
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.hacia_json(), 201


    def delete(self, id):
        proveedor = db.session.query(ProveedoresModels).get_or_404(id)
        db.session.delete(proveedor)
        db.session.commit()
        return '', 204

