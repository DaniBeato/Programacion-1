from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuariosModels
from main.auth.decoradores import admin_required, cliente_required, admin_or_cliente_required



class Clientes(Resource):
    @admin_required
    def get(self):
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        clientes = db.session.query(UsuariosModels).filter(UsuariosModels.rol == 'cliente')
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    clientes = clientes.filter(UsuariosModels.nombre == valor)
                if clave == 'apellido':
                    clientes = clientes.filter(UsuariosModels.apellido == valor)
        clientes = clientes.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Clientes': [cliente.hacia_json() for cliente in clientes.items],
                        'Cantidad total de clientes': clientes.total,
                        'Cantidad de páginas': clientes.pages,
                        'Página actual': pagina
                        })






class Cliente(Resource):
    @admin_required
    def get(self, id):
        cliente = db.session.query(UsuariosModels).get_or_404(id)
        if cliente.rol == 'cliente':
            return cliente.hacia_json()

    @cliente_required
    def put(self, id):
        cliente = db.session.query(UsuariosModels).get_or_404(id)
        if cliente.rol == 'cliente':
            datos = request.get_json().items()
            for clave, valor in datos:
                setattr(cliente, clave, valor)
            db.session.add(cliente)
            db.session.commit()
            return cliente.hacia_json()

    @admin_or_cliente_required
    def delete(self, id):
        cliente = db.session.query(UsuariosModels).get_or_404(id)
        if cliente.rol == 'cliente':
            db.session.delete(cliente)
            db.session.commit()
            return '', 204

