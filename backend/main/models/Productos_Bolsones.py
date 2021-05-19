from .. import db

class Productos_Bolsones(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    producto_ID = db.Column(db.Integer, nullable = False)
    bolson_ID = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '< Producto_ID: %r, Bolsón_ID: %r >' % (self.produtco_ID, self.bolson_ID)


    def hacia_json(self):
        producto_bolson_json = {
            'id': self.id,
            'producto_ID': self.producto_ID,
            'bolson_ID': self.bolson_ID,

        }
        return producto_bolson_json

    def desde_json(producto_bolson_json):
        id = producto_bolson_json.get('id')
        producto_ID = producto_bolson_json.get('producto_ID')
        bolson_ID = producto_bolson_json.get('bolson_ID')
        return Productos_Bolsones(id = id,
                                  producto_ID = producto_ID,
                                  bolson_ID = bolson_ID,
                                  )

