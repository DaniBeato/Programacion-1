from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels
from main.auth.decoradores import admin_required, proveedor_required, admin_or_proveedor_required, verificacion_token_revocado




class BolsonesPendientes(Resource):
    @admin_or_proveedor_required
    @verificacion_token_revocado
    def get(self):
        filtros = request.data
        bolsones_pendientes = db.session.query(BolsonesModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'nombre':
                    bolsones = bolsones_pendientes.filter(BolsonesModels.nombre == valor, BolsonesModels.estado == False)
        bolsones_pendientes= bolsones_pendientes.filter(BolsonesModels.estado == False)
        return jsonify({'Bolsones Pendientes': [bolson.hacia_json() for bolson in bolsones_pendientes]})

    @admin_required
    @verificacion_token_revocado
    def post(self):
        bolson_pendiente = BolsonesModels.desde_json(request.get_json())
        db.session.add(bolson_pendiente)
        db.session.commit()
        return bolson_pendiente.hacia_json(), 201




class BolsonPendiente(Resource):
    @admin_or_proveedor_required
    @verificacion_token_revocado
    def get(self, id):
        bolson_pendiente = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_pendiente.estado == False:
            return bolson_pendiente.hacia_json()
        else:
            return 'Este bolsón se encuentra aprobado'

    @admin_required
    @verificacion_token_revocado
    def delete(self, id):
        bolson_pendiente = db.session.query(BolsonesModels).get_or_404(id)
        if bolson_pendiente.estado == False:
            db.session.delete(bolson_pendiente)
            db.session.commit()
            return '', 204
        else:
            return 'Este bolsón se encuentra aprobado'

    @admin_required
    @verificacion_token_revocado
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


