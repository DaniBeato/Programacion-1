from .. import jwt
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "admin":
            return fn(*args, **kwargs)
        else:
            return 'Solo administradores tienen acceso', 403
    return wrapper


def proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "proveedor":
            return fn(*args, **kwargs)
        else:
            return 'Solo proveedores tienen acceso'
    return wrapper



def cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "cliente":
            return fn(*args, **kwargs)
        else:
            return 'Solo clientes tienen acceso'
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
                return 'Solo administradores o proveedores tienen acceso'
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
                return 'Solo administradores o clientes tienen acceso'
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