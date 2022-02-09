from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuariosModels
from main.auth.decoradores import admin_required, verificacion_token_revocado





class Administradores(Resource):
    #@admin_required
    #@verificacion_token_revocado
    def get(self):
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        administradores = db.session.query(UsuariosModels).filter(UsuariosModels.rol == 'admin')
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    administradores = administradores.filter(UsuariosModels.nombre == valor)
                if clave == 'apellido':
                    administradores = administradores.filter(UsuariosModels.apellido == valor)
        administradores = administradores.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Administradores': [administrador.hacia_json() for administrador in administradores.items],
                        'Cantidad total de administradores': administradores.total,
                        'Cantidad de páginas': administradores.pages,
                        'Página actual': pagina
                        })






class Administrador(Resource):
    #@admin_required
    #@verificacion_token_revocado
    def get(self, id):
        administrador = db.session.query(UsuariosModels).get_or_404(id)
        if administrador.rol == 'admin':
            return administrador.hacia_json()

    #@admin_required
    #@verificacion_token_revocado
    def put(self, id):
        administrador = db.session.query(UsuariosModels).get_or_404(id)
        if administrador.rol == 'admin':
            datos = request.get_json().items()
            for clave, valor in datos:
                setattr(administrador, clave, valor)
            db.session.add(administrador)
            db.session.commit()
            return administrador.hacia_json()

    #@admin_required
    #@verificacion_token_revocado
    def delete(self, id):
        administrador = db.session.query(UsuariosModels).get_or_404(id)
        if administrador.rol == 'admin':
            db.session.delete(administrador)
            db.session.commit()
            return '', 204

