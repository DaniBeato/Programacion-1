from .. import db
from datetime import datetime




class Token_revocado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)



