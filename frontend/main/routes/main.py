from flask import Blueprint, render_template, redirect, url_for, current_app, request, make_response, flash
import requests, json
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
from ..forms.registro_forms import RegistroForm
from ..forms.ingreso_forms import IngresoForm
from .auth import User
from .auth import admin_required

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def vista_principal():
    data = {}
    data['pagina'] = 1
    data['cantidad_elementos'] = 1
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones',
        headers={"content-type":"application/json"},
        data=json.dumps(data))
    print(r.text)
    bolsones = json.loads(r.text)['Bolsones']
    return render_template('/main/Vista_principal(1).html', bolsones = bolsones)
    #return render_template('/main/Vista_principal(1).html'


@main.route('/envio_ofertas')
def envio_ofertas():
    return render_template('/main/Envio_ofertas(6).html')


@main.route('/registro', methods=['POST', "GET"])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        data = {}
        data["nombre"] = form.nombre.data
        data["apellido"] = form.apellido.data
        data["mail"] = form.email.data
        data['telefono'] = form.telefono.data
        data["contrasenia"] = form.contrasenia.data
        data["rol"] = form.rol.data
        print(data)
        #auth = request.cookies['access_token']
        headers = {
            'content-type': "application/json",
            #'authorization': "Bearer " + auth
        }
        r = requests.post(
            current_app.config["API_URL"]+'/auth/register',
            headers = headers,
            data = json.dumps(data))
        return redirect(url_for('main.vista_principal'))
    print(form.errors)
    return render_template('/main/Registro(2).html', form = form)



@main.route('/ingreso', methods=['POST', "GET"])
def ingreso():
    form = IngresoForm()
    if form.validate_on_submit():
        data = {}
        data["mail"] = form.email.data
        data["contrasenia"] = form.contrasenia.data
        #data = '{"email":"' + form.email.data + '", "password":"' + form.password.data + '"}'
        print(data)
        #auth = request.cookies['access_token']
        headers = {
            'content-type': "application/json",
            #'authorization': "Bearer " + auth
        }
        r = requests.post(
            current_app.config["API_URL"] + '/auth/login',
            headers=headers,
            data=json.dumps(data))
        if r.status_code == 200:
            datos_usuario = json.loads(r.text)
            print('datos usuario', datos_usuario)
            usuario = User(id = datos_usuario.get("id"), email = datos_usuario.get("email"), rol = datos_usuario.get("rol"))
            login_user(usuario)
            req = make_response(redirect(url_for('main.vista_principal')))
            req.set_cookie('access_token', datos_usuario.get("token_acceso"), httponly = True)
            return req
        else:
            flash('Usuario o contraseña incorrecta', 'danger')
    print(form.errors)
    #return redirect(url_for('main.vista_principal'))
    return render_template('/main/Ingreso(3).html', form=form)



@main.route('/menu')
def menu():
    return render_template('/main/Menu(cliente)(31).html')


