from flask import Blueprint,render_template

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def vista_principal():
    return render_template('/main/Vista_principal(1).html')

@main.route('/envio_ofertas')
def envio_ofertas():
    return render_template('/main/Envio_ofertas(6).html')

@main.route('/registro')
def registro():
    return render_template('/main/Registro(2).html')

@main.route('/ingreso')
def ingreso():
    return render_template('/main/Ingreso(3).html')


