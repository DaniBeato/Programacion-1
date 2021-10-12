from flask import Blueprint, render_template, redirect, url_for, current_app
import requests, json
from ..forms.registro_forms import RegistroForm

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def vista_principal():
    data = {}
    data['pagina'] = 1
    data['cantidad_elementos'] = 10
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
        data["contaseña"] = form.contrasenia.data
        data["rol"] = form.rol.data
        print(data)
        headers = {
            'content-type': "application/json"
        }






    return render_template('/main/Registro(2).html')



@main.route('/ingreso')
def ingreso():
    return render_template('/main/Ingreso(3).html')


