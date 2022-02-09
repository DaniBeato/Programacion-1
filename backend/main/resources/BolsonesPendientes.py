from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels
from main.auth.decoradores import admin_required, proveedor_required, admin_or_proveedor_required, verificacion_token_revocado




class BolsonesPendientes(Resource):
    #@admin_or_proveedor_required
    #@verificacion_token_revocado
    def get(self):
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        bolsones_pendientes = db.session.query(BolsonesModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    bolsones_pendientes = bolsones_pendientes.filter(BolsonesModels.nombre == valor)
                if clave == 'estado':
                    bolsones_pendientes = bolsones_pendientes.filter(BolsonesModels.estado == valor)
        bolsones_pendientes = bolsones_pendientes.filter(BolsonesModels.estado == False)
        bolsones_pendientes = bolsones_pendientes.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Bolsones Pendientes': [bolson_pendiente.hacia_json() for bolson_pendiente in bolsones_pendientes.items],
                        'Cantidad total de bolsones pendientes': bolsones_pendientes.total,
                        'Cantidad de páginas': bolsones_pendientes.pages,
                        'Página actual': pagina
                        })
    #@admin_required
    #@verificacion_token_revocado
    def post(self):
        bolson_pendiente = BolsonesModels.desde_json(request.get_json())
        db.session.add(bolson_pendiente)
        db.session.commit()
        return bolson_pendiente.hacia_json(), 201




class BolsonPendiente(Resource):
    #@admin_or_proveedor_required
    #@verificacion_token_revocado
    def get(self, id):
        bolson_pendiente = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_pendiente.estado == False:
            return bolson_pendiente.hacia_json()
        else:
            return 'Este bolsón se encuentra aprobado', 400

    #@admin_required
    #@verificacion_token_revocado
    def delete(self, id):
        bolson_pendiente = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_pendiente.estado == False:
            db.session.delete(bolson_pendiente)
            db.session.commit()
            return '', 204
        else:
            return 'Este bolsón se encuentra aprobado'

    #@admin_required
    #@verificacion_token_revocado
    def put(self, id):
        bolson_pendiente = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_pendiente.estado == False:
            datos = request.get_json().items()
            for clave, valor in datos:
                setattr(bolson_pendiente, clave, valor)
            db.session.add(bolson_pendiente)
            db.session.commit()
            return bolson_pendiente.hacia_json(), 201
        else:
            return 'Este bolsón se encuentra aprobado'


