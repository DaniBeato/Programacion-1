from .. import login_manager
from flask import  flash, redirect, url_for,current_app
from flask_login import UserMixin, LoginManager, current_user
import jwt
from functools import wraps

class User(UserMixin):
    def __init__(self, id, email, rol):
        self.id = id
        self.email = email
        self.rol = rol


@login_manager.request_loader
def load_user(request):
    if 'access_token' in request.cookies:
        try:
            decoded = jwt.decoded = jwt.decode(request.cookies['access_token'], current_app.config["SECRET_KEY"], algorithm=["HS256"], verify=False)
            user = User(decoded["id"], decoded["email"], decoded["role"])
            return user
        except jwt.exceptions.InvalidTokenError:
            print('Token Inválido')
        except jwt.exceptions.DecodeError:
            print('Error de Decodificación')
    return None


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Debe iniciar sesión para continuar','warning')
    return redirect((url_for('main.vista_principal')))


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.role == "admin":
            flash('Acceso restringido a administradores.', 'warning')
            return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)
    return wrapper


def proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.role == "proveedor":
            flash('Acceso restringido a proveedores.','warning')
            return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)
    return wrapper


def cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.role == "cliente":
            flash('Acceso restringido a clientes.', 'warning')
            return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)

    return wrapper


def admin_or_proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_user.role != "admin":
            flash('Acceso restringido a administradores.', 'warning')
            return redirect(url_for('main.vista_principal'))
        else:
            if current_user.role != "proveedor":
                flash('Acceso restringido a proveedores.', 'warning')
                return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)
    return wrapper



def admin_or_cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_user.role != "admin":
            flash('Acceso restringido a administradores.', 'warning')
            return redirect(url_for('main.vista_principal'))
        else:
            if current_user.role != "cliente":
                flash('Acceso restringido a clientes.', 'warning')
                return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)
    return wrapper

