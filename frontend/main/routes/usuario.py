from flask import Blueprint, render_template, redirect, url_for, current_app, request
import requests, json
from .auth import admin_required



usuario = Blueprint('usuario', __name__, url_prefix = '/usuario')


#@admin_required
@usuario.route('/administradores')
def administradores():
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/administradores',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    administradores = json.loads(r.text)['Administradores']
    header = "Lista de Administradores"
    url = 'usuario.administrador'
    ths_list = ['nombre', 'apellido']
    return render_template('/usuario/Administradores_lista(4).html', objects = administradores, header = header, url = url, ths_list = ths_list, first_dict = 0)


#@admin_required
@usuario.route('/administrador/<int:id>')
def administrador(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/administrador/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.administradores'))
    administrador = json.loads(r.text)
    header = "Administrador"
    return render_template('/usuario/Administrador(5).html', object = administrador, header = header)


#@admin_required
@usuario.route('/editar_administrador')
def editar_administrador():
    data = {}
    # data['pagina'] = "1"
    # data['cantidad_elementos'] = "1"
    # auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer "  # + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/administradores',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    administradores = json.loads(r.text)['Administradores']
    header = "Editar Administrador"
    features = ['nombre', 'apellido', 'mail', 'contrasenia']
    return render_template('/usuario/Editar_administrador(36).html', objects = administradores, header = header, features = features, first_dict = 0)


#@admin_required
@usuario.route('/clientes')
def clientes():
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/clientes',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    clientes = json.loads(r.text)['Clientes']
    header = "Lista de Clientes"
    ths_list = ['nombre', 'apellido']
    url = 'usuario.cliente'
    return render_template('/usuario/Clientes_lista(17).html', objects = clientes, header = header, ths_list = ths_list, url = url, first_dict = 0)


#@admin_required
@usuario.route('/cliente/<int:id>')
def cliente(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/cliente/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.clientes'))
    cliente = json.loads(r.text)
    header = 'Cliente'
    return render_template('/usuario/Cliente(18).html', object = cliente, header = header)


#@admin_required
@usuario.route('/editar_cliente')
def editar_cliente():
    data = {}
    # data['pagina'] = "1"
    # data['cantidad_elementos'] = "1"
    # auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer "  # + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/clientes',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    clientes = json.loads(r.text)['Clientes']
    header = "Editar Cliente"
    features = ['nombre', 'apellido', 'mail', 'contrasenia']
    return render_template('/usuario/Editar_cliente(35).html', objects = clientes, header = header, features = features, first_dict = 0)


#@admin_required
@usuario.route('/compras')
def compras():
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer "# + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/compras',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    compras = json.loads(r.text)['Compras']
    header = 'Lista de Compras'
    url = 'usuario.compra'
    ths_list = ['fecha_compra', 'retirado']
    return render_template('/usuario/Compras_lista(19).html', objects = compras, header = header, url = url, ths_list = ths_list, first_dict = 0)


#@admin_required
@usuario.route('/compra/<int:id>')
def compra(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/compra/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.compras'))
    compra = json.loads(r.text)
    header = 'Compra'
    return render_template('/usuario/Compra(20).html', object = compra, header = header)


#@admin_required
@usuario.route('/proveedores')
def proveedores():
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/proveedores',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    proveedores = json.loads(r.text)['Proveedores']
    header = 'Lista de Proveedores'
    url = 'usuario.proveedor'
    ths_list = ['nombre', 'apellido']
    return render_template('/usuario/Proveedores_lista(23).html', objects = proveedores, header = header, url = url, ths_list = ths_list, first_dict = 0)


#@admin_required
@usuario.route('/proveedor/<int:id>')
def proveedor(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/proveedor/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.proveedores'))
    proveedor = json.loads(r.text)
    header = 'Proveedor'
    return render_template('/usuario/Proveedor(24).html', object = proveedor, header = header)


#@admin_required
@usuario.route('/editar_proveedor')
def editar_proveedor():
    data = {}
    # data['pagina'] = "1"
    # data['cantidad_elementos'] = "1"
    # auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer "  # + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/proveedores',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    proveedores = json.loads(r.text)['Proveedores']
    header = 'Editar Proveedor'
    features = ['nombre', 'apellido', 'mail', 'contrasenia']
    return render_template('/usuario/Editar_proveedor(34).html', objects = proveedores, header = header, features = features, first_dict = 0)















