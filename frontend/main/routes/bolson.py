from flask import flash, Blueprint, render_template, redirect, url_for, current_app, request
import requests, json
from flask_login import current_user
from .auth import admin_required, admin_or_proveedor_required, token_vencido, admin_or_cliente_required
from main.forms.bolson_forms import BolsonFilter
from main.forms.bolson_forms import BolsonForm
from main.forms.bolson_forms import BolsonFormEdit
from main.forms.producto_forms import ProductoForm
from main.forms.producto_forms import ProductoFilter
from datetime import datetime

bolson = Blueprint('bolson', __name__, url_prefix='/bolson')


@bolson.route('/bolsones')
@token_vencido
@admin_required
def bolsones():
    filter = BolsonFilter(request.args, meta={'csrf': False})
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
    if 'pagina' in request.args:
        # Si se han usado los botones de paginación cargar nueva página
        data["pagina"] = request.args.get('pagina', '')
    if filter.submit():
        if filter.nombre.data != '':
            data["nombre"] = filter.nombre.data
        print(filter.nombre.data)
        if filter.estado.data != None and filter.estado.data != '':
            if filter.estado.data == str('No aprobado'):
                data["estado"] = 0
            else:
                data["estado"] = 1
        print(filter.estado.data)
        if filter.desde.data != None:
            data["desde"] = filter.desde.data.strftime('%d/%m/%Y')
        print(filter.desde.data)
        if filter.hasta.data != None:
            data["hasta"] = filter.hasta.data.strftime('%d/%m/%Y')
        print(filter.hasta.data)
    print(data)

    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    # print(headers)

    r = requests.get(
        current_app.config["API_URL"] + '/bolsones',
        headers=headers,
        data=json.dumps(data))
    if (r.status_code == 404) or (r.status_code == 401):
        return redirect(url_for('main.vista_principal'))

    bolsones = json.loads(r.text)['Bolsones']
    # print(bolsones)
    paginacion = {}
    paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
    paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

    # print(bolsones[0]['nombre'])
    header = "Lista de Bolsones"
    url = "bolson.bolson_"
    ths_list = ["nombre", "estado", "fecha"]
    url_actual = 'bolson.bolsones'
    return render_template('/bolson/Bolsones_lista(7).html', objects=bolsones, header=header, url=url,
                           ths_list=ths_list, first_dict=0, paginacion=paginacion, filter=filter, url_actual=url_actual)


@bolson.route('/bolson/<int:id>')
@token_vencido
@admin_required
def bolson_(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolson/' + str(id),
        headers=headers)
    if (r.status_code == 404):
        return redirect(url_for('bolson.bolsones'))
    bolson = json.loads(r.text)
    header = "Bolsón"
    return render_template('/bolson/Bolson(8).html', object=bolson, header=header)


@bolson.route('/bolsones_pendientes', methods=['POST', "GET"])
@token_vencido
@admin_or_proveedor_required
def bolsones_pendientes():
    filter = BolsonFilter(request.args, meta={'csrf': False})
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
    if 'pagina' in request.args:
        # Si se han usado los botones de paginación cargar nueva página
        data["pagina"] = request.args.get('pagina', '')
    if filter.submit():
        if filter.nombre.data != '':
            data["nombre"] = filter.nombre.data
        # print(filter.nombre.data)
        if filter.desde.data != None:
            data["desde"] = filter.desde.data.strftime('%d/%m/%Y')
        # print(filter.desde.data)
        if filter.hasta.data != None:
            data["hasta"] = filter.hasta.data.strftime('%d/%m/%Y')
        # print(filter.hasta.data)
    # print(data)

    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }

    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-pendientes',
        headers=headers,
        data=json.dumps(data))
    # print(r.text)
    bolsones_pendientes = json.loads(r.text)['Bolsones Pendientes']
    paginacion = {}
    paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
    paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]
    print(paginacion)
    # print(bolsones_pendientes)
    header = 'Lista de Bolsones Pendientes'
    url = "bolson.bolson_pendiente"
    url_actual = "bolson.bolsones_pendientes"
    ths_list = ["nombre", "estado", "fecha"]
    return render_template('/bolson/Bolsones_pendientes_lista(admin)(38).html', objects=bolsones_pendientes,
                           header=header, url=url,
                           ths_list=ths_list, first_dict=0, paginacion=paginacion, filter=filter, url_actual=url_actual)
    # return render_template('/bolson/Bolsones_pendientes_lista(9).html', header = header, objects = bolsones_pendientes, url = url, feature = feature)


@bolson.route('/bolson_pendiente/<int:id>')
@token_vencido
@admin_or_proveedor_required
def bolson_pendiente(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-pendiente/' + str(id),
        headers=headers)
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_pendientes'))
    bolson_pendiente = json.loads(r.text)
    print(bolson_pendiente)
    header = 'Bolsón Pendiente'
    return render_template('/bolson/Bolson_pendiente(10).html', object=bolson_pendiente, header=header)


@bolson.route('/crear_editar_bolson_pendiente/<int:id>', methods=['POST', "GET", "PUT", 'DELETE'])
@token_vencido
@admin_required
def crear_editar_bolson_pendiente(id):
    form = BolsonForm()  # Instanciar formulario
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    if form.validate_on_submit():  # Si el formulario ha sido enviado y es validado correctamente

        data = {}
        data["nombre"] = form.nombre.data
        data["estado"] = form.estado.data
        data["fecha"] = form.fecha.data.strftime('%d/%m/%Y')

        if id == 0:
            r = requests.post(
                current_app.config["API_URL"] + '/bolsones-pendientes',
                headers=headers,
                data=json.dumps(data))
            print('Request devuelta', r.text)
            bolson_ID = json.loads(r.text)['id']
            productos = [form.producto.data, form.producto2.data, form.producto3.data, form.producto4.data]
            for producto in productos:
                if producto != 0:
                    print('it works')
                    data = {
                        'producto_ID': producto,
                        'bolson_ID': int(bolson_ID)
                    }
                    r = requests.post(current_app.config["API_URL"] + '/bolsones-productos',
                                      headers=headers,
                                      data=json.dumps(data))
            print(r.text)
            if r.status_code == 204:
                flash('Bolsón pendiente creado.', 'warning')
                return redirect(url_for('bolson.bolsones_pendientes'))
            else:
                flash('Error.', 'warning')
                return redirect(url_for('bolson.bolsones_pendientes'))
        else:
            r = requests.put(
                current_app.config["API_URL"] + '/bolson-pendiente/' + str(id),
                headers=headers,
                data=json.dumps(data))


            print(r.text)
            if r.status_code == 200:
                flash('Bolsón pendiente actualizado.', 'warning')
                return redirect(url_for('bolson.bolsones_pendientes'))
            else:
                flash('Error.', 'warning')
                return redirect(url_for('bolson.bolsones_pendientes'))
    else:
        if id == 0:
            data = {}
            data['pagina'] = 1

            header = 'Crear Bolsón Pendiente'
            auth = request.cookies['token_acceso']
            headers = {
                'content-type': "application/json",
                'authorization': "Bearer {}".format(auth)
            }

            r = requests.get(
                current_app.config["API_URL"] + '/productos',
                headers=headers,
                data=json.dumps(data))

            productos = [(item['id'], item['nombre']) for item in json.loads(r.text)["Productos"]]
            productos.insert(0, (0, ''))
            form.producto.choices = productos
            form.producto2.choices = productos
            form.producto3.choices = productos
            form.producto4.choices = productos

            return render_template('/bolson/Crear-editar_bolson_pendiente(32).html', id=0, form=form, header=header)
        else:
            form = BolsonFormEdit()
            auth = request.cookies['token_acceso']
            header = 'Editar Bolsón Pendiente'
            headers = {
                'content-type': "application/json",
                'authorization': "Bearer {}".format(auth)
            }
            r = requests.get(
                current_app.config["API_URL"] + '/bolson-pendiente/' + str(id),
                headers=headers)
            bolson_pendiente = json.loads(r.text)
            print(bolson_pendiente)
            return render_template('/bolson/Crear-editar_bolson_pendiente(32).html', id=bolson_pendiente['id'],
                                   form=form, header=header)


@bolson.route('/eliminar_bolson_pendiente/<int:id>')
@token_vencido
@admin_required
def eliminar_bolson_pendiente(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.delete(
        current_app.config["API_URL"] + '/bolson-pendiente/' + str(id),
        headers=headers)
    if r.status_code == 204:
        flash('Bolsón eliminado.', 'warning')
        return redirect(url_for('bolson.bolsones_pendientes'))
    else:
        flash('Error', 'warning')
        return redirect(url_for('bolson.bolsones_pendientes'))


@bolson.route('/bolsones_previos')
@token_vencido
@admin_required
def bolsones_previos():
    filter = BolsonFilter(request.args, meta={'csrf': False})
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
    if 'pagina' in request.args:
        # Si se han usado los botones de paginación cargar nueva página
        data["pagina"] = request.args.get('pagina', '')
    if filter.submit():
        if filter.nombre.data != '':
            data["nombre"] = filter.nombre.data
        print(filter.nombre.data)
        if filter.estado.data != None and filter.estado.data != '':
            if filter.estado.data == str('No aprobado'):
                data["estado"] = 0
            else:
                data["estado"] = 1
        print(filter.estado.data)
        if filter.desde.data != None:
            data["desde"] = filter.desde.data.strftime('%d/%m/%Y')
        print(filter.desde.data)
        if filter.hasta.data != None:
            data["hasta"] = filter.hasta.data.strftime('%d/%m/%Y')
        print(filter.hasta.data)
    print(data)

    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    # print(headers)

    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-previos',
        headers=headers,
        data=json.dumps(data))

    bolsones_previos = json.loads(r.text)['Bolsones Previos']
    paginacion = {}
    paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
    paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

    header = "Lista de Bolsones Previos"
    url = "bolson.bolson_previo"
    ths_list = ["nombre", "estado", "fecha"]
    url_actual = "bolson.bolsones_previos"
    return render_template('/bolson/Bolsones_previos_lista(11).html', objects=bolsones_previos, header=header, url=url,
                           ths_list=ths_list, first_dict=0,
                           paginacion=paginacion, filter=filter, url_actual=url_actual)


@bolson.route('/bolson_previo/<int:id>')
@token_vencido
@admin_required
def bolson_previo(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-previo/' + str(id),
        headers=headers)
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_previos'))
    bolson_previo = json.loads(r.text)
    header = "Bolsón Previo"
    return render_template('/bolson/Bolson_previo(12).html', object=bolson_previo, header=header)


@bolson.route('/bolsones_en_venta')
def bolsones_en_venta():
    filter = BolsonFilter(request.args, meta={'csrf': False})
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
    if 'pagina' in request.args:
        # Si se han usado los botones de paginación cargar nueva página
        data["pagina"] = request.args.get('pagina', '')
    if filter.submit():
        if filter.nombre.data != '':
            data["nombre"] = filter.nombre.data
        print(filter.nombre.data)
    print(data)

    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    # print(headers)

    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-venta',
        headers=headers,
        data=json.dumps(data))

    print(r.text)
    bolsones_venta = json.loads(r.text)['Bolsones Venta']
    # print(bolsones)
    paginacion = {}
    paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
    paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

    header = "Bolsones en Venta"
    url = "bolson.bolson_en_venta"
    feature = "nombre"
    url_actual = "bolson.bolsones_en_venta"
    print(bolsones_venta)
    if current_user.is_anonymous:
        return render_template('/bolson/Bolsones_venta(cliente)_lista(13).html', header=header, objects=bolsones_venta,
                               url=url, feature=feature,
                               paginacion=paginacion, filter=filter, url_actual=url_actual)
    elif current_user.rol=='admin':
        ths_list = ["nombre", "estado", "fecha"]
        return render_template('/bolson/Bolsones_venta(admin)_lista(15).html', objects = bolsones_venta, header = header ,url = url, filter=filter,
                               ths_list = ths_list, first_dict = 0, url_actual=url_actual, paginacion=paginacion,)
    else:
        return render_template('/bolson/Bolsones_venta(cliente)_lista(13).html', header=header, objects=bolsones_venta,
                               url=url, feature=feature,
                               paginacion=paginacion, filter=filter, url_actual=url_actual)
    # ths_list = ["nombre", "estado"]
    # return render_template('/bolson/Bolsones_venta(admin)_lista(15).html', objects = bolsones_venta, header = header ,url = url, ths_list = ths_list, first_dict = 0)


@bolson.route('/bolson_en_venta/<int:id>')
def bolson_en_venta(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-venta/' + str(id),
        headers=headers)
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_en_venta'))
    bolson_venta = json.loads(r.text)
    print(r.text)
    header = "Bolsón en Venta"
    return render_template('/bolson/Bolson_venta(cliente)(14).html', object=bolson_venta, header=header)


@bolson.route('/productos')
def productos():
    if current_user.is_anonymous:
        filter = ProductoFilter(request.args, meta={'csrf': False})
        data = {}
        data['pagina'] = "1"
        data['cantidad_elementos'] = "5"
        if 'pagina' in request.args:
            # Si se han usado los botones de paginación cargar nueva página
            data["pagina"] = request.args.get('pagina', '')
        if filter.submit():
            if filter.nombre.data != '':
                data["nombre"] = filter.nombre.data
            print(filter.nombre.data)
        print(data)

        auth = request.cookies['token_acceso']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(auth)
        }
        # print(headers)

        r = requests.get(
            current_app.config["API_URL"] + '/productos',
            headers=headers,
            data=json.dumps(data))
        print(r.text)
        productos = json.loads(r.text)['Productos']

        paginacion = {}
        paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
        paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

        header = 'Lista de Productos'
        feature = "nombre"
        url = 'bolson.producto'
        ths_list = ['nombre', 'id']
        url_actual = 'bolson.productos'
        return render_template('/bolson/Productos_lista(21).html', objects=productos, url=url, header=header,
                               ths_list=ths_list, first_dict=0,
                               paginacion=paginacion, filter=filter, url_actual=url_actual, feature=feature)
    elif current_user.rol == "admin" or current_user.rol == 'cliente':
        filter = ProductoFilter(request.args, meta={'csrf': False})
        data = {}
        data['pagina'] = "1"
        data['cantidad_elementos'] = "5"
        if 'pagina' in request.args:
            # Si se han usado los botones de paginación cargar nueva página
            data["pagina"] = request.args.get('pagina', '')
        if filter.submit():
            if filter.nombre.data != '':
                data["nombre"] = filter.nombre.data
            print(filter.nombre.data)
        print(data)

        auth = request.cookies['token_acceso']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(auth)
        }
        # print(headers)

        r = requests.get(
            current_app.config["API_URL"] + '/productos',
            headers=headers,
            data=json.dumps(data))
        print(r.text)
        productos = json.loads(r.text)['Productos']

        paginacion = {}
        paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
        paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

        header = 'Lista de Productos'
        feature = "nombre"
        url = 'bolson.producto'
        ths_list = ['nombre', 'id']
        url_actual = 'bolson.productos'
        return render_template('/bolson/Productos_lista(21).html', objects=productos, url=url, header=header,
                               ths_list=ths_list, first_dict=0,
                               paginacion=paginacion, filter=filter, url_actual=url_actual, feature=feature)
    else:
        filter = ProductoFilter(request.args, meta={'csrf': False})
        data = {}
        data['pagina'] = "1"
        data['cantidad_elementos'] = "5"
        data['usuario_ID'] = current_user.id
        if 'pagina' in request.args:
            # Si se han usado los botones de paginación cargar nueva página
            data["pagina"] = request.args.get('pagina', '')
        if filter.submit():
            if filter.nombre.data != '':
                data["nombre"] = filter.nombre.data
            print(filter.nombre.data)
        print(data)

        auth = request.cookies['token_acceso']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(auth)
        }
        # print(headers)

        r = requests.get(
            current_app.config["API_URL"] + '/productos',
            headers=headers,
            data=json.dumps(data))
        print(r.text)
        productos = json.loads(r.text)['Productos']

        paginacion = {}
        paginacion["cantidad_paginas"] = json.loads(r.text)["Cantidad de páginas"]
        paginacion["pagina_actual"] = json.loads(r.text)["Página actual"]

        header = 'Lista de Productos'
        feature = "nombre"
        url = 'bolson.producto'
        ths_list = ['nombre', 'id']
        url_actual = 'bolson.productos'
        return render_template('/bolson/Productos_lista(21).html', objects=productos, url=url, header=header,
                               ths_list=ths_list, first_dict=0,
                               paginacion=paginacion, filter=filter, url_actual=url_actual, feature=feature)



@bolson.route('/producto/<int:id>')
def producto(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " "Bearer {}".format(auth)
    }
    r = requests.get(
        current_app.config["API_URL"] + '/producto/' + str(id),
        headers=headers)
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.productos'))
    producto = json.loads(r.text)
    print(r.text)
    header = 'Producto'
    return render_template('/bolson/Producto(22).html', object=producto, header=header)


@bolson.route('/crear_editar_producto/<int:id>', methods=['POST', "GET", "PUT"])
@token_vencido
@admin_or_proveedor_required
def crear_editar_producto(id):
    form = ProductoForm()  # Instanciar formulario
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "5"
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

    proveedores = [(item['id'], item['nombre']) for item in json.loads(r.text)["Proveedores"]]
    proveedores.insert(0, (0, ''))
    form.usuario_ID.choices = proveedores

    if form.validate_on_submit():  # Si el formulario ha sido enviado y es validado correctamente
        data = {}
        data["nombre"] = form.nombre.data
        data["usuario_ID"] = form.usuario_ID.data
        print(data)
        auth = request.cookies['token_acceso']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(auth)
        }
        if id == 0:
            r = requests.post(
                current_app.config["API_URL"] + '/productos',
                headers=headers,
                data=json.dumps(data))
            print('data', data)
            print('request', r.text)
            print('token', auth)
            print('headers', headers)
            if r.status_code == 201:
                flash('Producto creado.', 'warning')
                return redirect(url_for('bolson.productos'))
            else:
                flash('Error.', 'warning')
                return redirect(url_for('bolson.productos'))
        else:
            r = requests.put(
                current_app.config["API_URL"] + '/producto/' + str(id),
                headers=headers,
                data=json.dumps(data))
            print(r.text)
            if r.status_code == 201:
                flash('Producto actulizado.', 'warning')
                return redirect(url_for('bolson.productos'))
            else:
                flash('Error.', 'warning')
                return redirect(url_for('bolson.productos'))
    else:
        if id == 0:
            header = 'Crear Producto'
            return render_template('/bolson/Crear-editar_producto(33).html', id=0, form=form, header=header)
        else:
            header = 'Editar Producto'
            auth = request.cookies['token_acceso']
            headers = {
                'content-type': "application/json",
                'authorization': "Bearer {}".format(auth)
            }
            r = requests.get(
                current_app.config["API_URL"] + '/producto/' + str(id),
                headers=headers)
            producto = json.loads(r.text)
            print(producto)
            return render_template('/bolson/Crear-editar_producto(33).html', id=producto['id'],
                                   form=form, header=header)


@bolson.route('/eliminar_producto/<int:id>')
@token_vencido
@admin_required
def eliminar_producto(id):
    auth = request.cookies['token_acceso']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {}".format(auth)
    }
    '''
    r = requests.get(
        current_app.config["API_URL"] + '/producto/' + str(id),
        headers=headers)
    if r.text['']
    '''
    r = requests.delete(
        current_app.config["API_URL"] + '/producto/' + str(id),
        headers=headers)
    if r.status_code == 201:
        flash('Producto eliminado.', 'warning')
        return redirect(url_for('bolson.productos'))
    else:
        flash('Error', 'warning')
        return redirect(url_for('bolson.productos'))
