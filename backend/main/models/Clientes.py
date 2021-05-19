from .. import db

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(100), nullable = False)
    mail = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return '< Nombre: %r, Apellido: %r, Teléfono: %r, Mail: %r >' % (self.nombre, self.apellido, self.telefono, self.mail)

    def hacia_json(self):
       cliente_json = {
           'id': self.id,
           'nombre': self.nombre,
           'apellido': self.apellido,
           'telefono': self.telefono,
           'mail': self.mail,

       }
       return cliente_json

    def desde_json(cliente_json):
        id = cliente_json.get('id')
        nombre = cliente_json.get('nombre')
        apellido = cliente_json.get('apellido')
        telefono = cliente_json.get('telefono')
        mail = cliente_json.get('mail')
        return Clientes(id = id,
                        nombre = nombre,
                        apellido = apellido,
                        telefono = telefono,
                        mail = mail,
                        )

