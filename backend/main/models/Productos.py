from .. import db

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    proveedor_ID = db.Column(db.Integer, nullable = False)
    nombre = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return '< Proveedor_ID: %r, Nombre: %r >' % (self.proveedor_ID, self.nombre)


    def hacia_json(self):
        producto_json = {
            'id': self.id,
            'proveedor_ID': self.proveedor_ID,
            'nombre': self.nombre
        }
        return producto_json

    def desde_json(producto_json):
        id = producto_json.get('id')
        proveedor_ID = producto_json.get('proveedor_ID')
        nombre = producto_json.get('nombre')
        return Productos(id = id,
            proveedor_ID = proveedor_ID,
            nombre = nombre,
            )
