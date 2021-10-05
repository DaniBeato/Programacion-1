from flask import Blueprint, render_template, current_app
import requests, json

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

@main.route('/registro')
def registro():
    return render_template('/main/Registro(2).html')

@main.route('/ingreso')
def ingreso():
    return render_template('/main/Ingreso(3).html')

