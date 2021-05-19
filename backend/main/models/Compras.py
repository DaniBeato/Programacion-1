from .. import db
from datetime import datetime

class Compras(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    clienteID = db.Column(db.Integer, nullable = False)
    bolsonID = db.Column(db.Integer, nullable = False)
    fecha_compra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)


    def __repr__(self):
        return '< ClienteID: %r, BolsónID: %r, Fecha y hora de compra: %r, Retirado: %r >' % (self.clienteID, self.bolsonID, self.fecha_compra, self.retirado)


    def hacia_json(self):
        compra_json = {
            'id': self.id,
            'clienteID': self.clienteID,
            'bolsonID': self.bolsonID,
            'fecha_compra': self.fecha_compra.strftime('%d/%m/%Y'),
            'retirado': self.retirado,
        }
        return compra_json

    def desde_json(compra_json):
        id = compra_json.get('id')
        clienteID = compra_json.get('clienteID')
        bolsonID = compra_json.get('bolsonID')
        fecha_compra = datetime.strptime(compra_json.get('fecha_compra'), '%d/%m/%Y')
        retirado = compra_json.get('retirado')
        return Compras(id = id,
                       clienteID = clienteID,
                       bolsonID = bolsonID,
                       fecha_compra = fecha_compra,
                       retirado = retirado,
                       )

