from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonesModels





class Bolsones(Resource):
    def get(self):
        bolsones = db.session.query(BolsonesModels).all()
        return jsonify([bolson.hacia_json() for bolson in bolsones])




class Bolson(Resource):
    def get(self,id):
       bolson = db.session.query(BolsonesModels).get_or_404(id)
       return bolson.hacia_json()
