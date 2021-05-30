from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClientesModels



class Clientes(Resource):
    def get(self):
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        clientes = db.session.query(ClientesModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    clientes = clientes.filter(ClientesModels.nombre == valor)
                if clave == 'apellido':
                    clientes = clientes.filter(ClientesModels.apellido == valor)
        clientes = clientes.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Clientes': [cliente.hacia_json() for cliente in clientes.items],
                        'Cantidad total de clientes': clientes.total,
                        'Cantidad de páginas': clientes.pages,
                        'Página actual': pagina
                        })



    def post(self):
        cliente = ClientesModels.desde_json(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente.hacia_json(), 201


class Cliente(Resource):
    def get(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        return cliente.hacia_json()

    def put(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(cliente, clave, valor)
        db.session.add(cliente)
        db.session.commit()
        return cliente.hacia_json()

    def delete(self, id):
        cliente = db.session.query(ClientesModels).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204

