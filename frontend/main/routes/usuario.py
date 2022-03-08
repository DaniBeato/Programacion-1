from flask import Blueprint, render_template, redirect, url_for, current_app, request
import requests, json
from .auth import admin_required, admin_or_proveedor_required, admin_or_cliente_required
from main.forms.usuario_forms import UsuarioForm
from main.forms.usuario_forms import UsuarioFilter
from main.forms.compra_forms import CompraForm
from main.forms.compra_forms import CompraFilter




usuario = Blueprint('usuario', __name__, url_prefix = '/usuario')


@admin_required
@usuario.route('/administradores')
def administradores():
    filter = UsuarioFilter(request.args, meta={'csrf': False})
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
    if 'pagina' in request.args:
        # Si se han usado los botones de paginación cargar nueva página
        data["pagina"] = request.args.get('pagina', '')
    if filter.submit():
        filter_list_p = []
        if filter.nombre.data != '':
            data["nombre"] = filter.nombre.data
            nombre = filter.nombre.data
            filter_list_p.append(nombre)
        if filter.apellido.data != '':
            data["apellido"] = filter.apellido.data
            apellido = filter.apellido.data
            filter_list_p.append(apellido)
        print(filter.apellido.data)
    print(data)

    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    # print(headers)

    r = requests.get(
        current_app.config["API_URL"] + '/administradores',
        headers=headers,
        data=json.dumps(data))

    print(r.text)
    administradores = json.loads(r.text)['Administradores']
    paginacion = {}
    paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
    paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

    header = "Lista de Administradores"
    url = 'usuario.administrador'
    ths_list = ['nombre', 'apellido']
    url_actual = 'usuario.administradores'
    return render_template('/usuario/Administradores_lista(4).html', objects = administradores, header = header, url = url, ths_list = ths_list, first_dict = 0,
                           paginacion = paginacion, filter = filter, filter_list_p = filter_list_p, url_actual = url_actual)


@admin_required
@usuario.route('/administrador/<int:id>')
def administrador(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/administrador/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.administradores'))
    administrador = json.loads(r.text)
    header = "Administrador"
    return render_template('/usuario/Administrador(5).html', object = administrador, header = header)


@admin_required
@usuario.route('/editar_administrador/<int:id>', methods=["GET", "PUT", "POST"])
def editar_administrador(id):
    form = UsuarioForm()  # Instanciar formulario
    if form.validate_on_submit():  # Si el formulario ha sido enviado y es validado correctamente
        data = {}
        data["nombre"] = form.nombre.data
        data["apellido"] = form.apellido.data
        data["mail"] = form.email.data
        data['telefono'] = form.telefono.data
        data["contrasenia"] = form.contrasenia.data
        data["rol"] = form.rol.data
        print(data)
        auth = request.cookies['token_acceso']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(auth)
        }
        r = requests.put(
            current_app.config["API_URL"] + '/administrador/' + str(id),
            headers=headers,
            data=json.dumps(data))
        print(r.text)
        return redirect(url_for('usuario.administradores'))
    header = "Editar Administrador"
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/administrador/' + str(id),
        headers=headers)
    administrador = json.loads(r.text)
    print(administrador)
    url = 'usuario.editar_administrador'
    return render_template('/usuario/Editar_usuario(34).html', id=administrador['id'],
                           form=form, header=header, url = url)

@admin_required
@usuario.route('/clientes')
def clientes():
    filter = UsuarioFilter(request.args, meta={'csrf': False})
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
    if 'pagina' in request.args:
        # Si se han usado los botones de paginación cargar nueva página
        data["pagina"] = request.args.get('pagina', '')
    if filter.submit():
        filter_list_p = []
        if filter.nombre.data != '':
            data["nombre"] = filter.nombre.data
            nombre = filter.nombre.data
            filter_list_p.append(nombre)
        if filter.apellido.data != '':
            data["apellido"] = filter.apellido.data
            apellido = filter.apellido.data
            filter_list_p.append(apellido)
        print(filter.apellido.data)
    print(data)

    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    # print(headers)

    r = requests.get(
        current_app.config["API_URL"] + '/clientes',
        headers=headers,
        data=json.dumps(data))

    print(r.text)
    paginacion = {}
    paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
    paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]


    clientes = json.loads(r.text)['Clientes']
    header = "Lista de Clientes"
    ths_list = ['nombre', 'apellido']
    url = 'usuario.cliente'
    url_actual = 'usuario.clientes'
    return render_template('/usuario/Clientes_lista(17).html', objects = clientes, header = header, ths_list = ths_list, url = url, first_dict = 0,
                           paginacion = paginacion, filter = filter, filter_list_p = filter_list_p, url_actual = url_actual)


@admin_or_cliente_required
@usuario.route('/cliente/<int:id>')
def cliente(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/cliente/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.clientes'))
    cliente = json.loads(r.text)
    header = 'Cliente'
    return render_template('/usuario/Cliente(18).html', object = cliente, header = header)


@admin_or_cliente_required
@usuario.route('/editar_cliente/<int:id>', methods=["GET", "PUT", "POST"])
def editar_cliente(id):
    form = UsuarioForm()  # Instanciar formulario
    if form.validate_on_submit():  # Si el formulario ha sido enviado y es validado correctamente
        data = {}
        data["nombre"] = form.nombre.data
        data["apellido"] = form.apellido.data
        data["mail"] = form.email.data
        data['telefono'] = form.telefono.data
        data["contrasenia"] = form.contrasenia.data
        data["rol"] = form.rol.data
        print(data)
        auth = request.cookies['token_acceso']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(auth)
        }
        r = requests.put(
            current_app.config["API_URL"] + '/cliente/' + str(id),
            headers=headers,
            data=json.dumps(data))
        print(r.text)
        return redirect(url_for('usuario.clientes'))
    header = "Editar Cliente"
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/cliente/' + str(id),
        headers=headers)
    cliente = json.loads(r.text)
    print(cliente)
    url = 'usuario.editar_cliente'
    return render_template('/usuario/Editar_usuario(34).html', id=cliente['id'],
                           form=form, header=header, url = url)
@admin_or_cliente_required
@usuario.route('/compras')
def compras():
    filter = CompraFilter(request.args, meta={'csrf': False})
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
    if 'pagina' in request.args:
        # Si se han usado los botones de paginación cargar nueva página
        data["pagina"] = request.args.get('pagina', '')
    if filter.submit():
        filter_list_p = []
        if filter.usuario_ID.data != '' and filter.usuario_ID.data != None:
            data["usuario_ID"] = filter.usuario_ID.data
            usuario_ID = filter.usuario_ID.data
            filter_list_p.append(usuario_ID)
        if filter.retirado.data != '' and filter.retirado.data != None:
            data["retirado"] = filter.retirado.data
            retirado = filter.retirado.data
            filter_list_p.append(retirado)
    print(data)

    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    # print(headers)

    r = requests.get(
        current_app.config["API_URL"] + '/compras',
        headers=headers,
        data=json.dumps(data))

    print(r.text)

    paginacion = {}
    paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
    paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

    compras = json.loads(r.text)['Compras']
    print(compras)
    header = 'Lista de Compras'
    url = 'usuario.compra'
    ths_list = ['id','fecha_compra', 'retirado']
    url_actual = 'usuario.compras'
    return render_template('/usuario/Compras_lista(19).html', objects = compras, header = header, url = url, ths_list = ths_list, first_dict = 0,
                           paginacion = paginacion, filter = filter, filter_list_p = filter_list_p, url_actual = url_actual)


@admin_or_cliente_required
@usuario.route('/compra/<int:id>')
def compra(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/compra/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.compras'))
    compra = json.loads(r.text)
    header = 'Compra'
    return render_template('/usuario/Compra(20).html', object = compra, header = header)


@admin_required
@usuario.route('/editar_compra/<int:id>', methods=["GET", "PUT", "POST"])
def editar_compra(id):
    form = CompraForm()  # Instanciar formulario
    if form.validate_on_submit():  # Si el formulario ha sido enviado y es validado correctamente
        data = {}
        data["usuario_ID"] = form.usuario_ID.data
        data["bolson_ID"] = form.bolsonID.data
        data["retirado"] = form.retirado.data
        data['fecha_compra'] = form.fecha_compra.data.strftime('%d/%m/%Y')
        print(data)
        auth = request.cookies['token_acceso']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(auth)
        }
        r = requests.put(
            current_app.config["API_URL"] + '/compra/' + str(id),
            headers=headers,
            data=json.dumps(data))
        print(r.text)
        return redirect(url_for('usuario.compras'))
    header = "Editar Compra"
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/compra/' + str(id),
        headers=headers)
    compra = json.loads(r.text)
    print(compra)
    return render_template('/usuario/Editar_compra(35).html', id=compra['id'],
                           form=form, header=header)


@usuario.route('/proveedores')
def proveedores():
    filter = UsuarioFilter(request.args, meta={'csrf': False})
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
    if 'pagina' in request.args:
        # Si se han usado los botones de paginación cargar nueva página
        data["pagina"] = request.args.get('pagina', '')
    if filter.submit():
        filter_list_p = []
        if filter.nombre.data != '':
            data["nombre"] = filter.nombre.data
            nombre = filter.nombre.data
            filter_list_p.append(nombre)
        if filter.apellido.data != '':
            data["apellido"] = filter.apellido.data
            apellido = filter.apellido.data
            filter_list_p.append(apellido)
        print(filter.apellido.data)
    print(data)

    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    # print(headers)

    r = requests.get(
        current_app.config["API_URL"] + '/proveedores',
        headers=headers,
        data=json.dumps(data))
    print(r.text)

    paginacion = {}
    paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
    paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

    proveedores = json.loads(r.text)['Proveedores']
    header = 'Lista de Proveedores'
    url = 'usuario.proveedor'
    ths_list = ['nombre', 'apellido']
    url_actual = 'usuario.proveedores'
    return render_template('/usuario/Proveedores_lista(23).html', objects = proveedores, header = header, url = url, ths_list = ths_list, first_dict = 0,
                           paginacion = paginacion, filter = filter, filter_list_p = filter_list_p, url_actual = url_actual)


admin_or_proveedor_required
@usuario.route('/proveedor/<int:id>')
def proveedor(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/proveedor/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('usuario.proveedores'))
    proveedor = json.loads(r.text)
    header = 'Proveedor'
    return render_template('/usuario/Proveedor(24).html', object = proveedor, header = header)


@admin_or_proveedor_required
@usuario.route('/editar_proveedor/<int:id>', methods=["GET", "PUT", "POST"])
def editar_proveedor(id):
    form = UsuarioForm()  # Instanciar formulario
    if form.validate_on_submit():  # Si el formulario ha sido enviado y es validado correctamente
        data = {}
        data["nombre"] = form.nombre.data
        data["apellido"] = form.apellido.data
        data["mail"] = form.email.data
        data['telefono'] = form.telefono.data
        data["contrasenia"] = form.contrasenia.data
        data["rol"] = form.rol.data
        print(data)
        auth = request.cookies['token_acceso']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(auth)
        }
        r = requests.put(
            current_app.config["API_URL"] + '/proveedor/' + str(id),
            headers=headers,
            data=json.dumps(data))
        print(r.text)
        return redirect(url_for('usuario.proveedores'))
    header = "Editar Proveedor"
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/proveedor/' + str(id),
        headers=headers)
    proveedor = json.loads(r.text)
    print(proveedor)
    url = 'usuario.editar_proveedor'
    return render_template('/usuario/Editar_usuario(34).html', id=proveedor['id'],
                           form=form, header=header, url=url)














