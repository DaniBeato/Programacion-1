from .. import login_manager
from flask import  flash, redirect, url_for,current_app
from flask_login import UserMixin, LoginManager, current_user
import jwt
from functools import wraps

class User(UserMixin):
    def __init__(self, id, mail, rol):
        self.id = id
        self.mail = mail
        self.rol = rol


@login_manager.request_loader
def load_user(request):
    if 'token_acceso' in request.cookies:
        try:
            print(request.cookies['token_acceso'])
            print(current_app.config["SECRET_KEY"])
            decoded = jwt.decode(request.cookies['token_acceso'], current_app.config["SECRET_KEY"], algorithm=["HS256"], verify=False)
            print(decoded)
            user = User(decoded["id"], decoded["mail"], decoded["rol"])
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
        if not current_user.rol == "admin":
            flash('Acceso restringido a administradores.', 'warning')
            return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)
    return wrapper


def proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.rol == "proveedor":
            flash('Acceso restringido a proveedores.','warning')
            return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)
    return wrapper


def cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.rol == "cliente":
            flash('Acceso restringido a clientes.', 'warning')
            return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)

    return wrapper


def admin_or_proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_user.rol != "admin":
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
        if current_user.rol != "admin":
            flash('Acceso restringido a administradores.', 'warning')
            return redirect(url_for('main.vista_principal'))
        else:
            if current_user.rol != "cliente":
                flash('Acceso restringido a clientes.', 'warning')
                return redirect(url_for('main.vista_principal'))
        return fn(*args, **kwargs)
    return wrapper



