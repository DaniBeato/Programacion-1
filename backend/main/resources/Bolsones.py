from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels
from main.auth.decoradores import admin_required, verificacion_token_revocado








class Bolsones(Resource):
    #@admin_required
    #@verificacion_token_revocado
    def get(self):
        pagina = 1
        cantidad_elementos = 10
        filtros = request.data
        bolsones = db.session.query(BolsonesModels)
        if filtros:
            for clave, valor in request.get_json().items():
                if clave == 'pagina':
                    pagina = int(valor)
                if clave == 'cantidad_elementos':
                    cantidad_elementos = int(valor)
                if clave == 'nombre':
                    bolsones = bolsones.filter(BolsonesModels.nombre == valor)
                if clave == 'estado':
                    bolsones = bolsones.filter(BolsonesModels.estado == valor)
        bolsones = bolsones.paginate(pagina, cantidad_elementos, True, 30)
        return jsonify({'Bolsones': [bolson.hacia_json() for bolson in bolsones.items],
                        'Cantidad total de bolsones': bolsones.total,
                        'Cantidad de páginas': bolsones.pages,
                        'Página actual': pagina
                        })





class Bolson(Resource):
    @admin_required
    @verificacion_token_revocado
    def get(self,id):
       bolson = db.session.query(BolsonesModels).get_or_404(id)
       return bolson.hacia_json()
