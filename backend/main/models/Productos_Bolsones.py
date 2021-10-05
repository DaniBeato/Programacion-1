from .. import db
from . import BolsonesModels
from . import ProductosModels

class Productos_Bolsones(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    producto_ID = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable = False)
    bolson_ID = db.Column(db.Integer, db.ForeignKey("bolsones.id"), nullable = False)
    bolsones = db.relationship("Bolsones", back_populates = "productos_bolsones", uselist = False, single_parent = True)
    productos = db.relationship("Productos", back_populates = "productos_bolsones", uselist = False, single_parent = True)

    def __repr__(self):
        return '< Producto_ID: %r, Bolsón_ID: %r >' % (self.producto_ID, self.bolson_ID)


    def hacia_json(self):
        self.bolson = db.session.query(BolsonesModels).get_or_404(self.bolson_ID)
        self.producto = db.session.query(ProductosModels).get_or_404(self.producto_ID)
        producto_bolson_json = {
            'id': self.id,
            #'producto_ID': self.producto_ID,
            #'bolson_ID': self.bolson_ID,
            'bolson': self.bolson.hacia_json(),
            'producto': self.producto.hacia_json()
        }
        return producto_bolson_json

    @staticmethod
    def desde_json(producto_bolson_json):
        id = producto_bolson_json.get('id')
        producto_ID = producto_bolson_json.get('producto_ID')
        bolson_ID = producto_bolson_json.get('bolson_ID')
        return Productos_Bolsones(id = id,
                                  producto_ID = producto_ID,
                                  bolson_ID = bolson_ID,
                                  )

