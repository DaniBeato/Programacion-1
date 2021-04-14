from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'Nombre': 'Mixfrutal'},
    2: {'Nombre': 'Mixvegetal'},
}



class Bolsones(Resource):
    def get(self):
        return BOLSONES
    def post(self):
        bolson = request.get_json()
        id = int(max(BOLSONES.keys())) + 1
        BOLSONES[id] = bolson
        return BOLSONES[id], 201


class Bolson(Resource):
    def get(self,id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404