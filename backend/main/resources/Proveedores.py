from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuariosModels
from main.auth.decoradores import admin_required, proveedor_required, admin_or_proveedor_required, verificacion_token_revocado



class Proveedores(Resource):
    def get(self):
        filtros = request.data
        proveedores = db.session.query(UsuariosModels).filter(UsuariosModels.rol == 'proveedor')
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'nombre':
                    proveedores = proveedores.filter(UsuariosModels.nombre == valor)
        proveedores = proveedores.all()
        return jsonify({'Proveedores': [proveedor.hacia_json() for proveedor in proveedores]})




class Proveedor(Resource):
    @admin_or_proveedor_required
    @verificacion_token_revocado
    def get(self, id):
        proveedor = db.session.query(UsuariosModels).get_or_404(id)
        if proveedor.rol == 'proveedor':
            return proveedor.hacia_json()

    @admin_required
    @verificacion_token_revocado
    def put(self, id):
        proveedor = db.session.query(UsuariosModels).get_or_404(id)
        if proveedor.rol == 'proveedor':
            datos = request.get_json().items()
            for clave, valor in datos:
                setattr(proveedor, clave, valor)
            db.session.add(proveedor)
            db.session.commit()
            return proveedor.hacia_json(), 201

    @admin_required
    @verificacion_token_revocado
    def delete(self, id):
        proveedor = db.session.query(UsuariosModels).get_or_404(id)
        if proveedor.rol == 'proveedor':
            db.session.delete(proveedor)
            db.session.commit()
            return '', 204

