from .. import db
from datetime import datetime
from . import UsuariosModels
from . import BolsonesModels

class Compras(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario_ID = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable = False)
    bolsonID = db.Column(db.Integer, db.ForeignKey('bolsones.id'), nullable = False)
    fecha_compra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)
    usuarios = db.relationship("Usuarios", back_populates = "compras", uselist = False, single_parent = True)
    bolsones = db.relationship("Bolsones", back_populates = "compras", uselist = False, single_parent = True)

    def __repr__(self):
        return '< Usuario_ID: %r, BolsónID: %r, Fecha y hora de compra: %r, Retirado: %r >' % (self.usuario_ID, self.bolsonID, self.fecha_compra, self.retirado)


    def hacia_json(self):
        self.usuario = db.session.query(UsuariosModels).get_or_404(self.usuario_ID)
        self.bolson = db.session.query(BolsonesModels).get_or_404(self.bolsonID)
        compra_json = {
            'id': self.id,
            #'usuario_ID': self.usuario_ID,
            #'bolsonID': self.bolsonID,
            'fecha_compra': self.fecha_compra.strftime('%d/%m/%Y'),
            'retirado': self.retirado,
            'usuario': self.usuario.hacia_json(),
            'bolson': self.bolson.hacia_json()
        }
        return compra_json

    @staticmethod
    def desde_json(compra_json):
        id = compra_json.get('id')
        usuario_ID = compra_json.get('usuario_ID')
        bolsonID = compra_json.get('bolsonID')
        fecha_compra = datetime.strptime(compra_json.get('fecha_compra'), '%d/%m/%Y')
        retirado = compra_json.get('retirado')
        return Compras(id = id,
                       usuario_ID = usuario_ID,
                       bolsonID = bolsonID,
                       fecha_compra = fecha_compra,
                       retirado = retirado,
                       )

