from .. import db
from . import ProveedoresModels

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    proveedor_ID = db.Column(db.Integer, db.ForeignKey("proveedores.id"), nullable = False)
    nombre = db.Column(db.String(100), nullable = False)
    proveedores = db.relationship("Proveedores", back_populates = "productos", uselist = False, single_parent = True)
    productos_bolsones = db.relationship("Productos_Bolsones", back_populates="productos",cascade="all, delete-orphan")

    def __repr__(self):
        return '< Proveedor_ID: %r, Nombre: %r >' % (self.proveedor_ID, self.nombre)


    def hacia_json(self):
        self.proveedores = db.session.query(ProveedoresModels).get_or_404(self.proveedor_ID)
        producto_json = {
            'id': self.id,
            #'proveedor_ID': self.proveedor_ID,
            'nombre': self.nombre,
            'proveedores': self.proveedores.hacia_json()
        }
        return producto_json

    @staticmethod
    def desde_json(producto_json):
        id = producto_json.get('id')
        proveedor_ID = producto_json.get('proveedor_ID')
        nombre = producto_json.get('nombre')
        return Productos(id = id,
            proveedor_ID = proveedor_ID,
            nombre = nombre,
            )
