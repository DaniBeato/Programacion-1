from .. import db
from datetime import datetime
from . import Productos_BolsonesModels

class Bolsones(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    precio = db.Column(db.String, nullable = False)
    estado = db.Column(db.Boolean, nullable = False)
    fecha = db.Column(db.DateTime, nullable = False)
    compras = db.relationship("Compras", back_populates = "bolsones", cascade = "all, delete-orphan")
    productos_bolsones = db.relationship("Productos_Bolsones", back_populates = "bolsones", cascade = "all, delete-orphan")



    def __repr__(self):
        return '< Nombre: %r, Fecha de creación: %r, Estado: %r, Productos: r%>' % (self.nombre, self.fecha, self.estado, self.productos_bolsones)

    def hacia_json(self):
        productos = [producto.hacia_json() for producto in self.productos_bolsones]
        bolson_json = {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'estado': self.estado,
            'fecha': self.fecha.strftime('%d/%m/%Y'),
            'productos': productos
        }
        return bolson_json

    @staticmethod
    def desde_json(bolson_json):
        id = bolson_json.get('id')
        nombre = bolson_json.get('nombre')
        precio = bolson_json.get('precio')
        estado = bolson_json.get('estado')
        fecha = datetime.strptime(bolson_json.get('fecha'), '%d/%m/%Y')
        bolson = Bolsones(id = id,
                      nombre = nombre,
                      precio = precio,
                      estado = estado,
                      fecha = fecha,
                      )
        if 'productos' in bolson_json:
            for producto_ID in bolson_json.get('productos'):
                bolson.productos.append(Productos_BolsonesModels.productos(producto_ID=producto_ID))
        return bolson

    @staticmethod
    def desde_json_ofertas(bolson_json):
        nombre = bolson_json.get('nombre')
        fecha = datetime.strptime(bolson_json.get('fecha'), '%d/%m/%Y')
        return Bolsones(nombre=nombre,
                        fecha=fecha,
                        )
