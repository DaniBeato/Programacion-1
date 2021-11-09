from flask import Blueprint, render_template, redirect, url_for, current_app, request
import requests, json
from .auth import admin_required



usuario = Blueprint('usuario', __name__, url_prefix = '/usuario')


@admin_required
@usuario.route('/administradores')
def administradores():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/administradores',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    administradores = json.loads(r.text)['Administradores']
    return render_template('/usuario/Administradores_lista(4).html', administradores=administradores)


@admin_required
@usuario.route('/administrador/<int:id>')
def administrador(id):
    auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/administrador/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.administradores'))
    administrador = json.loads(r.text)
    return render_template('/usuario/Administrador(5).html', administrador=administrador)


@admin_required
@usuario.route('/crear_editar_administrador')
def crear_editar_administrador():
    return render_template('/usuario/Crear-editar_administrador(36).html')


@admin_required
@usuario.route('/clientes')
def clientes():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/clientes',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    clientes = json.loads(r.text)['Clientes']
    return render_template('/usuario/Clientes_lista(17).html', clientes=clientes)


@admin_required
@usuario.route('/cliente/<int:id>')
def cliente(id):
    auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/cliente/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.clientes'))
    cliente = json.loads(r.text)
    return render_template('/usuario/Cliente(18).html', cliente=cliente)


@admin_required
@usuario.route('/editar_cliente')
def editar_cliente():
    return render_template('/usuario/Editar_cliente(35).html')


@admin_required
@usuario.route('/compras')
def compras():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/compras',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    compras = json.loads(r.text)['Compras']
    return render_template('/usuario/Compras_lista(19).html', compras=compras)


@admin_required
@usuario.route('/compra/<int:id>')
def compra(id):
    auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/compra/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.compras'))
    compra = json.loads(r.text)
    return render_template('/usuario/Compra(20).html', compra=compra)


@admin_required
@usuario.route('/proveedores')
def proveedores():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/proveedores',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    proveedores = json.loads(r.text)['Proveedores']
    return render_template('/usuario/Proveedores_lista(23).html', proveedores=proveedores)


@admin_required
@usuario.route('/proveedor/<int:id>')
def proveedor(id):
    auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/proveedor/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.proveedores'))
    proveedor = json.loads(r.text)
    return render_template('/usuario/Proveedor(24).html', proveedor=proveedor)


@admin_required
@usuario.route('/crear_editar_proveedor')
def crear_editar_proveedor():
    return render_template('/usuario/Crear-editar_proveedor(34).html')















