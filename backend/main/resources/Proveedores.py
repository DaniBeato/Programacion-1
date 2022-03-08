from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuariosModels
from werkzeug.security import generate_password_hash
from main.auth.decoradores import admin_required, proveedor_required, admin_or_proveedor_required, verificacion_token_revocado



class Proveedores(Resource):
    @admin_required
    def get(self):
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        proveedores = db.session.query(UsuariosModels).filter(UsuariosModels.rol == 'proveedor')
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    proveedores = proveedores.filter(UsuariosModels.nombre == valor)
                if clave == 'apellido':
                    proveedores = proveedores.filter(UsuariosModels.apellido == valor)
        proveedores = proveedores.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Proveedores': [proveedor.hacia_json() for proveedor in proveedores.items],
                        'Cantidad total de proveedores': proveedores.total,
                        'Cantidad de páginas': proveedores.pages,
                        'Página actual': pagina
                        })



class Proveedor(Resource):
    @admin_or_proveedor_required
    @verificacion_token_revocado
    def get(self, id):
        proveedor = db.session.query(UsuariosModels).get_or_404(id)
        if proveedor.rol == 'proveedor':
            return proveedor.hacia_json()

    @admin_or_proveedor_required
    @verificacion_token_revocado
    def put(self, id):
        proveedor = db.session.query(UsuariosModels).get_or_404(id)
        if proveedor.rol == 'proveedor':
            datos = request.get_json().items()
            for clave, valor in datos:
                if clave == 'contrasenia':
                    valor = generate_password_hash(valor)
                setattr(proveedor, clave, valor)
            db.session.add(proveedor)
            db.session.commit()
            return proveedor.hacia_json(), 204

    @admin_required
    @verificacion_token_revocado
    def delete(self, id):
        proveedor = db.session.query(UsuariosModels).get_or_404(id)
        if proveedor.rol == 'proveedor':
            db.session.delete(proveedor)
            db.session.commit()
            return '', 204

