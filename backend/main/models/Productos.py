from .. import db
from . import UsuariosModels

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario_ID = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable = False)
    nombre = db.Column(db.String(100), nullable = False)
    usuarios = db.relationship("Usuarios", back_populates = "productos", uselist = False, single_parent = True)
    productos_bolsones = db.relationship("Productos_Bolsones", back_populates="productos",cascade="all, delete-orphan")

    def __repr__(self):
        return '< Usuario_ID: %r, Nombre: %r >' % (self.usuario_ID, self.nombre)


    def hacia_json(self):
        #self.usuarios = db.session.query(UsuariosModels).get_or_404(self.usuario_ID)
        producto_json = {
            'id': self.id,
            'nombre': self.nombre,
            #'usuarios': self.usuarios.hacia_json()
        }
        return producto_json

    @staticmethod
    def desde_json(producto_json):
        id = producto_json.get('id')
        usuario_ID = producto_json.get('usuario_ID')
        nombre = producto_json.get('nombre')
        return Productos(id = id,
            usuario_ID = usuario_ID,
            nombre = nombre,
            )
