from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ComprasModels




class Compras(Resource):
    def get(self):
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        compras = db.session.query(ComprasModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'clienteID':
                    compras = compras.filter(ComprasModels.clienteID == valor)
                if clave == 'retirado':
                    compras = compras.filter(ComprasModels.retirado == valor)
        compras = compras.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Compras': [compra.hacia_json() for compra in compras.items],
                        'Cantidad total de compras': compras.total,
                        'Cantidad de páginas': compras.pages,
                        'Página actual': pagina
                        })

    def post(self):
        compra = ComprasModels.desde_json(request.get_json())
        db.session.add(compra)
        db.session.commit()
        return compra.hacia_json(), 201


class Compra(Resource):
    def get(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        return compra.hacia_json()


    def put(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(compra, clave, valor)
        db.session.add(compra)
        db.session.commit()
        return compra.hacia_json(), 201


    def delete(self, id):
        compra = db.session.query(ComprasModels).get_or_404(id)
        db.session.delete(compra)
        db.session.commit()
        return '', 204
