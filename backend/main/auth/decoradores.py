from .. import jwt
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps
from .. import db
from main.models import Token_revocadoModels







def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "admin":
            return fn(*args, **kwargs)
        else:
            return 'Solo administradores tienen acceso', 404
    return wrapper



def proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "proveedor":
            return fn(*args, **kwargs)
        else:
            return 'Solo proveedores tienen acceso', 404
    return wrapper




def cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "cliente":
            return fn(*args, **kwargs)
        else:
            return 'Solo clientes tienen acceso', 404
    return wrapper




def admin_or_proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "admin":
            return fn(*args, **kwargs)
        else:
            if claims['rol'] == "proveedor":
                return fn(*args, **kwargs)
            else:
                return 'Solo administradores o proveedores tienen acceso', 404
    return wrapper



def admin_or_cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "admin":
            return fn(*args, **kwargs)
        else:
            if claims['rol'] == "cliente":
                return fn(*args, **kwargs)
            else:
                return 'Solo administradores o clientes tienen acceso', 404
    return wrapper


@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return usuario.id

@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'rol': usuario.rol,
        'id': usuario.id,
        'mail': usuario.mail
    }
    return claims


def verificacion_token_revocado(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        jti = claims["jti"]
        token = db.session.query(Token_revocadoModels.id).filter_by(jti = jti).scalar()
        if token:
            return 'Este token es inválido porque el usuario ha cerrado sesión', 404
        else:
            return fn(*args, **kwargs)
    return wrapper
