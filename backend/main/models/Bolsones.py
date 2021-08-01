from .. import db
from datetime import datetime

class Bolsones(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    estado = db.Column(db.Boolean, nullable = False)
    fecha = db.Column(db.DateTime, nullable = False)
    compras = db.relationship("Compras", back_populates = "bolsones", cascade = "all, delete-orphan")
    productos_bolsones = db.relationship("Productos_Bolsones", back_populates = "bolsones", cascade = "all, delete-orphan")



    def __repr__(self):
        return '< Nombre: %r, Fecha de creación: %r >' % (self.nombre, self.fecha)

    def hacia_json(self):
        bolson_json = {
            'id': self.id,
            'nombre': self.nombre,
            'estado': self.estado,
            'fecha': self.fecha.strftime('%d/%m/%Y'),
        }
        return bolson_json

    @staticmethod
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

    @staticmethod
    def desde_json_ofertas(bolson_json):
        nombre = bolson_json.get('nombre')
        fecha = datetime.strptime(bolson_json.get('fecha'), '%d/%m/%Y')
        return Bolsones(nombre=nombre,
                        fecha=fecha,
                        )
