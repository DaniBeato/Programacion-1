from .. import db
from datetime import datetime
from . import ClientesModels
from . import BolsonesModels

class Compras(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    clienteID = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable = False)
    bolsonID = db.Column(db.Integer, db.ForeignKey('bolsones.id'), nullable = False)
    fecha_compra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)
    clientes = db.relationship("Clientes", back_populates = "compras", uselist = False, single_parent = True)
    bolsones = db.relationship("Bolsones", back_populates = "compras", uselist = False, single_parent = True)

    def __repr__(self):
        return '< ClienteID: %r, BolsónID: %r, Fecha y hora de compra: %r, Retirado: %r >' % (self.clienteID, self.bolsonID, self.fecha_compra, self.retirado)


    def hacia_json(self):
        self.cliente = db.session.query(ClientesModels).get_or_404(self.clienteID)
        self.bolson = db.session.query(BolsonesModels).get_or_404(self.bolsonID)
        compra_json = {
            'id': self.id,
            #'clienteID': self.clienteID,
            #'bolsonID': self.bolsonID,
            'fecha_compra': self.fecha_compra.strftime('%d/%m/%Y'),
            'retirado': self.retirado,
            'cliente': self.cliente.hacia_json(),
            'bolson': self.bolson.hacia_json()
        }
        return compra_json

    @staticmethod
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

