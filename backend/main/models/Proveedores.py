from .. import db

class Proveedores(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(100), nullable = False)
    productos = db.relationship("Productos", back_populates = "proveedores", cascade = "all, delete-orphan")


    def __repr__(self):
        return'< Nombre: %r, telefono: %r' % (self.nombre, self.telefono)


    def hacia_json(self):
        proveedor_json = {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono,

        }
        return proveedor_json

    @staticmethod
    def desde_json(proveedor_json):
        id = proveedor_json.get('id')
        nombre = proveedor_json.get('nombre')
        telefono = proveedor_json.get('telefono')
        return Proveedores(id = id,
                           nombre = nombre,
                           telefono = telefono,
                           )
