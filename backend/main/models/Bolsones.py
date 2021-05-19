from .. import db
from datetime import datetime

class Bolsones(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    estado = db.Column(db.String(100), nullable = False)
    fecha = db.Column(db.DateTime, nullable = False)


    def __repr__(self):
        return '< Nombre: %r, Estado: %r, Fecha: %r >' % (self.nombre, self.estado, self.fecha)

    def hacia_json(self):
        bolson_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'estado': str(self.estado),
            'fecha': self.fecha.strftime('%d/%m/%Y'),
        }
        return bolson_json


    def desde_json(bolson_json):
        id = bolson_json.get('id')
        nombre = bolson_json.get('nombre')
        estado = bolson_json.get('estado')
        fecha = datetime.strptime(bolson_json.get('fecha'), '%d/%m/%Y')
        return Bolsones(id = id,
                      nombre = nombre,
                      estado = estado,
                      fecha = fecha,
                      )



