
from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuariosModels
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from main.mail.Funciones import sendMail
from datetime import datetime
from main.models import Token_revocadoModels
import os



auth = Blueprint('auth', __name__, url_prefix = '/auth')


@auth.route('/login', methods = ['POST'])
def login():
    usuario = db.session.query(UsuariosModels).filter(UsuariosModels.mail == request.get_json().get("mail")).first_or_404()
    if usuario.validacion_contrasenia(request.get_json().get("contrasenia")):
        token_acceso = create_access_token(identity = usuario)
        datos = {
            'id': str(usuario.id),
            'mail': usuario.mail,
            'token_acceso': token_acceso,
            'rol': usuario.rol
        }
        return datos, 200
    else:
        return 'Contraseña incorrecta', 401

@auth.route('/register', methods = ['POST'])
def register():
    usuario = UsuariosModels.desde_json(request.get_json())
    existencia = db.session.query(UsuariosModels).filter(UsuariosModels.mail == usuario.mail).scalar() is not None
    if existencia:
        return 'Mail duplicado', 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
            sent = sendMail([usuario.mail], "¡Bienvenido!", 'Registro', usuario = usuario)
        except Exception as error:
            print(error)
            db.session.rollback()
            return str(error), 409
        return usuario.hacia_json(), 201




@auth.route("/logout/<id>", methods = ["DELETE"])
@jwt_required()
def logout(id):
    now = datetime.now()
    tokens = db.session.query(Token_revocadoModels).all()
    for token in tokens:
        if (now - (token.fecha_creacion)).seconds > int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES')):
            db.session.delete(token)
            db.session.commit()
    claims = get_jwt()
    if claims['id'] == int(id):
        jti = get_jwt()["jti"]
        db.session.add(Token_revocadoModels(jti = jti, fecha_creacion = now))
        db.session.commit()
        return jsonify(msg = "Se ha cerrado la sesión con éxito"), 200
    else:
        return 'Usted no puede dar de baja a otro usuario'





