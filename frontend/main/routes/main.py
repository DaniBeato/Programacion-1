from flask import Blueprint, render_template, redirect, url_for, current_app, request, make_response, flash
import requests, json
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
from ..forms.registro_forms import RegistroForm
from ..forms.ingreso_forms import IngresoForm
from .auth import User
from .auth import token_vencido

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def vista_principal():
    return redirect(url_for('bolson.bolsones_en_venta'))
    #return render_template('/main/Vista_principal(1).html'


@main.route('/envio_ofertas')
def envio_ofertas():
    return render_template('/main/Envio_ofertas(6).html')


@main.route('/registro', methods=['POST', "GET"])
def registro():
    form = RegistroForm()  # Instanciar formulario
    form.rol.choices = ["cliente", "proveedor"]
    if form.validate_on_submit():  # Si el formulario ha sido enviado y es validado correctamente
        data = {}
        data["nombre"] = form.nombre.data
        data["apellido"] = form.apellido.data
        data["mail"] = form.mail.data
        data['telefono'] = form.telefono.data
        data["contrasenia"] = form.contrasenia.data
        data["rol"] = form.rol.data
        # auth = request.cookies['access_token']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer" #+ auth
        }
        r = requests.post(
            current_app.config["API_URL"] + '/auth/register',
            headers=headers,
            data=json.dumps(data))
        #Inicio de sesión automático
        data = '{"mail":"' + form.mail.data + '", "contrasenia":"' + form.contrasenia.data + '"}'
        headers = {
            'content-type': "application/json",
        }
        r = requests.post(
            current_app.config["API_URL"] + '/auth/login',
            headers=headers,
            data=data)
        datos_usuario = json.loads(r.text)
        #print('datos usuario', datos_usuario)
        usuario = User(id=datos_usuario.get("id"), mail=datos_usuario.get("mail"), rol=datos_usuario.get("rol"))
        login_user(usuario)
        req = make_response(redirect(url_for('main.vista_principal')))
        req.set_cookie('token_acceso', datos_usuario.get("token_acceso"), httponly=True)
        flash('Registro e inicio de sesión correctos', 'warning')
        return req
    header = 'Registro'
    return render_template('main/Registro(2).html', form = form, header = header)  # Muestra el formulario



@main.route('/ingreso', methods=['POST', "GET"])
def ingreso():
    form = IngresoForm()
    if form.validate_on_submit():
        data = '{"mail":"' + form.mail.data + '", "contrasenia":"' + form.contrasenia.data + '"}'
        print(data)
        headers = {
            'content-type': "application/json",
        }
        r = requests.post(
            current_app.config["API_URL"] + '/auth/login',
            headers= headers,
            data= data)
        if r.status_code == 200:
            datos_usuario = json.loads(r.text)
            #print('datos usuario', datos_usuario)
            usuario = User(id = datos_usuario.get("id"), mail = datos_usuario.get("mail"), rol = datos_usuario.get("rol"))
            login_user(usuario)
            #print(login_user(usuario))
            #print('current user', current_user.rol)
            req = make_response(redirect(url_for('main.vista_principal')))
            req.set_cookie('token_acceso', datos_usuario.get("token_acceso"), httponly = True)
            flash('Inicio de sesión correcto', 'warning')
            return req
        else:
            flash('Usuario o contraseña incorrecta', 'warning')
    print(form.errors)
    header = 'Ingreso'
    #return redirect(url_for('main.vista_principal'))
    return render_template('/main/Ingreso(3).html', form=form, header = header)



@main.route('/cerrar_sesion')
@token_vencido
def cerrar_sesion():
    #Crear una request de redirección
    req = make_response(redirect(url_for('main.vista_principal')))
    #Vaciar cookie
    req.set_cookie('token_acceso', '', httponly = True)
    #Deloguear usuario
    logout_user()
    flash('Sesión cerrada con éxito', 'warning')
    #Realizar request
    return req


@main.route('/menu')
def menu():
    if current_user.is_anonymous:
        return render_template('/main/Menu_sin_registro(41).html')
    elif current_user.rol == "cliente":
        return render_template('/main/Menu(cliente)(31).html', id=current_user.id)
    elif current_user.rol == "proveedor":
        return render_template('/main/Menu(proveedor)(30).html', id=current_user.id)
    elif current_user.rol == "admin":
        return render_template('/main/Menu(administrador)(29).html', id=current_user.id)











