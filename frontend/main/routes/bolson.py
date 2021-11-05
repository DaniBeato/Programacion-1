from flask import Blueprint, render_template, redirect, url_for, current_app
import requests, json

bolson = Blueprint('bolson', __name__, url_prefix = '/bolson')


@bolson.route('/bolsones')
def bolsones():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones',
        headers={"content-type":"application/json"},
        data=json.dumps(data))
    print(r.text)
    bolsones = json.loads(r.text)['Bolsones']
    return render_template('/bolson/Bolsones_lista(7).html', bolsones = bolsones)


@bolson.route('/bolson/<int:id>')
def bolson_(id):
    r = requests.get(
        current_app.config["API_URL"]+'/bolson/'+str(id),
        headers={"content-type":"application/json"})
    if(r.status_code==404):
        return redirect(url_for('bolson.bolsones'))
    bolson = json.loads(r.text)
    return render_template('/bolson/Bolson(8).html', bolson = bolson)


@bolson.route('/bolsones_pendientes')
def bolsones_pendientes():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-pendientes',
        headers={"content-type": "application/json"},
        data=json.dumps(data))
    print(r.text)
    bolsones_pendientes = json.loads(r.text)['Bolsones Pendientes']
    return render_template('/bolson/Bolsones_pendientes_lista(9).html', bolsones_pendientes=bolsones_pendientes)

    '''filter = BolsonPendienteFilterForm(request.args, meta={'csrf': False})
    data = {}
    data['page'] = 1
    data['per_page'] = 10
    if 'page' in request.args:
        data["page"] = request.args.get('page', '')
    if filter.submit():
        if filter.yearFrom.data != None:
            data["year[gte]"] = filter.yearFrom.data.year
        if filter.yearTo.data != None:
            data["year[lte]"] = filter.yearTo.data.year
        print(filter.professorId.data)

    r = requests.get(
        current_app.config["API_URL"] + '/bolson',
        headers=headers,
        data=json.dumps(data))
    bolsones = json.loads(r.text)["Bolsones"]
    pagination = {}
    pagination["pages"] = json.loads(r.text)["pages"]
    pagination["current_page"] = json.loads(r.text)["page"]
    return render_template('/bolson/Bolson_pendiente(10).html', bolsones=bolsones, pagination=pagination, filter=filter)
'''


@bolson.route('/bolson_pendiente/<int:id>')
def bolson_pendiente(id):
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-pendiente/' + str(id),
        headers={"content-type": "application/json"})
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_pendientes'))
    bolson_pendiente = json.loads(r.text)
    return render_template('/bolson/Bolson_pendiente(10).html', bolson_pendiente=bolson_pendiente)



@bolson.route('/crear_editar_bolson_pendiente')
def crear_editar_bolson_pendiente():
    return render_template('/bolson/Crear-editar_bolson_pendiente(32).html')


@bolson.route('/bolsones_previos')
def bolsones_previos():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-previos',
        headers={"content-type": "application/json"},
        data=json.dumps(data))
    print(r.text)
    bolsones_previos = json.loads(r.text)['Bolsones Previos']
    return render_template('/bolson/Bolsones_previos_lista(11).html', bolsones_previos=bolsones_previos)


@bolson.route('/bolson_previo/<int:id>')
def bolson_previo(id):
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-previo/' + str(id),
        headers={"content-type": "application/json"})
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_previos'))
    bolson_previo = json.loads(r.text)
    return render_template('/bolson/Bolson_previo(12).html', bolson_previo=bolson_previo)


@bolson.route('/bolsones_en_venta')
def bolsones_en_venta():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-venta',
        headers={"content-type": "application/json"},
        data=json.dumps(data))
    print(r.text)
    bolsones_venta = json.loads(r.text)['Bolsones Venta']
    return render_template('/bolson/Bolsones_venta(cliente)_lista(13).html', bolsones_venta=bolsones_venta)


@bolson.route('/bolson_en_venta/<int:id>')
def bolson_en_venta(id):
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-venta/' + str(id),
        headers={"content-type": "application/json"})
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_en_venta'))
    bolson_venta = json.loads(r.text)
    print(r.text)
    return render_template('/bolson/Bolson_venta(cliente)(14).html', bolson_venta=bolson_venta)


@bolson.route('/productos')
def productos():
    data = {}
    data['pagina'] = "1"
    data['cantidad_elementos'] = "1"
    r = requests.get(
        current_app.config["API_URL"] + '/productos',
        headers={"content-type": "application/json"},
        data=json.dumps(data))
    print(r.text)
    productos = json.loads(r.text)['Productos']
    return render_template('/bolson/Productos_lista(21).html', productos=productos)


@bolson.route('/producto/<int:id>')
def producto(id):
    r = requests.get(
        current_app.config["API_URL"] + '/producto/' + str(id),
        headers={"content-type": "application/json"})
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.productos'))
    producto = json.loads(r.text)
    print(r.text)
    return render_template('/bolson/Producto(22).html', producto=producto)



@bolson.route('/crear_editar_producto')
def crear_editar_producto():
    return render_template('/bolson/Crear-editar_producto(33).html')




