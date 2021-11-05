from flask import Blueprint, render_template, redirect, url_for, current_app
import requests, json


usuario = Blueprint('usuario', __name__, url_prefix = '/usuario')


@usuario.route('/administradores')
def administradores():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    r = requests.get(
        current_app.config["API_URL"] + '/administradores',
        headers={"content-type": "application/json"},
        data=json.dumps(data))
    print(r.text)
    administradores = json.loads(r.text)['Administradores']
    return render_template('/usuario/Administradores_lista(4).html', administradores=administradores)


@usuario.route('/administrador/<int:id>')
def administrador(id):
    r = requests.get(
        current_app.config["API_URL"] + '/administrador/' + str(id),
        headers={"content-type": "application/json"})
    if (r.status_code == 404):
        return redirect(url_for('usuario.administradores'))
    administrador = json.loads(r.text)
    return render_template('/usuario/Administrador(5).html', administrador=administrador)


@usuario.route('/crear_editar_administrador')
def crear_editar_administrador():
    return render_template('/usuario/Crear-editar_administrador(36).html')


@usuario.route('/clientes')
def clientes():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    r = requests.get(
        current_app.config["API_URL"] + '/clientes',
        headers={"content-type": "application/json"},
        data=json.dumps(data))
    print(r.text)
    clientes = json.loads(r.text)['Clientes']
    return render_template('/usuario/Clientes_lista(17).html', clientes=clientes)


@usuario.route('/cliente')
def cliente():
    return render_template('/usuario/Cliente(18).html')


@usuario.route('/editar_cliente')
def editar_cliente():
    return render_template('/usuario/Editar_cliente(35).html')


@usuario.route('/compras')
def compras():
    return render_template('/usuario/Compras_lista(19).html')


@usuario.route('/compra')
def compra():
    return render_template('/usuario/Compra(20).html')


@usuario.route('/proveedores')
def proveedores():
    return render_template('/usuario/Proveedores_lista(23).html')


@usuario.route('/proveedor')
def proveedor():
    return render_template('/usuario/Proveedor(24).html')


@usuario.route('/crear_editar_proveedor')
def crear_editar_proveedor():
    return render_template('/usuario/Crear-editar_proveedor(34).html')















