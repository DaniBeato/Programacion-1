from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(100), nullable = False)
    mail = db.Column(db.String(100), unique = True, index = True, nullable = False)
    contrasenia = db.Column(db.String(100), nullable = False)
    rol = db.Column(db.String(100), nullable = False)
    compras = db.relationship("Compras", back_populates="usuarios", cascade="all, delete-orphan")
    productos = db.relationship("Productos", back_populates="usuarios", cascade="all, delete-orphan")



    def __repr__(self):
        return '< Nombre: %r, Apellido: %r, Teléfono: %r, Mail: %r, Contraseña %r, Rol: %r >' % (self.nombre,self.apellido, self.telefono, self.mail, self.contrasenia, self.rol)


    @property
    def contrasenia_plana(self):
        raise AttributeError('La contraseña no se puede mostrar')

    @contrasenia_plana.setter
    def contrasenia_plana(self, contrasenia):
        self.contrasenia = generate_password_hash(contrasenia)


    def validacion_contrasenia(self, contrasenia):
        return check_password_hash(self.contrasenia, contrasenia)




    def hacia_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'mail': self.mail,
            'contrasenia': self.contrasenia,
            'rol': self.rol,
        }
        return usuario_json

    @staticmethod
    def desde_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        telefono = usuario_json.get('telefono')
        mail = usuario_json.get('mail')
        contrasenia = usuario_json.get('contrasenia')
        rol = usuario_json.get('rol')
        return Usuarios(id = id,
                        nombre = nombre,
                        apellido = apellido,
                        telefono = telefono,
                        mail = mail,
                        contrasenia_plana = contrasenia,
                        rol = rol,
                        )