from flask import Blueprint, render_template, redirect, url_for, current_app, request
import requests, json
from .auth import admin_required
#from main.forms.filtro_forms import FiltroForm, BolsonForm

bolson = Blueprint('bolson', __name__, url_prefix = '/bolson')

#@admin_required
@bolson.route('/bolsones')
def bolsones():
    #filter = FiltroForm(request.args,meta={'csrf': False})
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer "#+auth
    }
    print(headers)
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones',
        headers = headers,
        data = json.dumps(data))


    #if filter.submit():
        #if filter.nombre.data != None:
            #data["nombre"] = filter.nombre.data
        #if filter.fecha.data != None:
            #data["fecha"] = filter.fecha.data
        #if filter.estado.data != None :
            #data["estado"] = filter.estado.data
    print(r.text)
    bolsones = json.loads(r.text)['Bolsones']
    print(bolsones[0]['nombre'])
    header = "Lista de Bolsones"
    url = "bolson.bolson_"
    ths_list = ["nombre", "estado"]
    return render_template('/bolson/Bolsones_lista(7).html', objects = bolsones, header = header, url = url, ths_list = ths_list, first_dict = 0)


#@admin_required
@bolson.route('/bolson/<int:id>')
def bolson_(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
        }
    r = requests.get(
        current_app.config["API_URL"]+'/bolson/'+str(id),
        headers = headers)
    if(r.status_code==404):
        return redirect(url_for('bolson.bolsones'))
    bolson = json.loads(r.text)
    header = "Bolsón"
    return render_template('/bolson/Bolson(8).html', object = bolson, header = header)


#@admin_required
@bolson.route('/bolsones_pendientes')
def bolsones_pendientes():
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-pendientes',
        headers = headers,
        data = json.dumps(data))
    print(r.text)
    bolsones_pendientes = json.loads(r.text)['Bolsones Pendientes']
    print(bolsones_pendientes)
    header = 'Lista de Bolsones Pendientes'
    url = "bolson.bolson_pendiente"
    ths_list = ["nombre", "estado"]
    return render_template('/bolson/Bolsones_pendientes_lista(admin)(38).html', objects = bolsones_pendientes, header = header, url = url, ths_list = ths_list, first_dict = 0)
    #feature = "nombre"
    #return render_template('/bolson/Bolsones_pendientes_lista(9).html', header = header, objects = bolsones_pendientes, url = url, feature = feature)

    '''

    #filter = BolsonPendienteFilterForm(request.args, meta={'csrf': False})
    data = {}
    #data['page'] = 1
    #data['per_page'] = 10
    #if 'page' in request.args:
    #    data["page"] = request.args.get('page', '')
    #if filter.submit():
    #    if filter.yearFrom.data != None:
    #        data["year[gte]"] = filter.yearFrom.data.year
    #    if filter.yearTo.data != None:
    #        data["year[lte]"] = filter.yearTo.data.year
    #    print(filter.professorId.data)

    r = requests.get(
        current_app.config["API_URL"] + '/bolson',
        headers=headers,
        data=json.dumps(data))
    bolsones_pendientes = json.loads(r.text)["Bolsones"]
    #pagination = {}
    #pagination["pages"] = json.loads(r.text)["pages"]
    #pagination["current_page"] = json.loads(r.text)["page"]
    #return render_template('/bolson/Bolson_pendiente(10).html', bolsones=bolsones, pagination=pagination, filter=filter)
    return render_template('/bolson/Bolsones_pendientes_lista(admin)(38).html', items=bolsones_pendientes)
    '''

#@admin_required
@bolson.route('/bolson_pendiente/<int:id>')
def bolson_pendiente(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-pendiente/' + str(id),
        headers = headers)
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_pendientes'))
    bolson_pendiente = json.loads(r.text)
    header = 'Bolsón Pendiente'
    return render_template('/bolson/Bolson_pendiente(10).html', object = bolson_pendiente, header = header)



#@admin_required
@bolson.route('/crear_editar_bolson_pendiente', methods=['POST', "GET"])
def crear_editar_bolson_pendiente():
    form = BolsonForm()  # Instanciar formulario
    if form.validate_on_submit():  # Si el formulario ha sido enviado y es validado correctamente
        data = {}
        data["nombre"] = form.nombre.data
        data["estado"] = form.estado.data
        data["fecha"] = form.fecha.data
        print(data)
        # auth = request.cookies['access_token']
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer"  # + auth
        }
        r = requests.post(
            current_app.config["API_URL"] + '/bolsones-pendientes',
            headers=headers,
            data=json.dumps(data))
        return redirect(url_for('bolson.bolsones'))  # Redirecciona a lista
    data = {}
    # data['pagina'] = "1"
    # data['cantidad_elementos'] = "1"
    # auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer "  # + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-pendientes',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    bolsones_pendientes = json.loads(r.text)['Bolsones Pendientes']
    print(bolsones_pendientes)
    header = 'Crear/Editar Bolsones Pendientes'
    features = ["nombre", "estado", "fecha"]
    return render_template('/bolson/Crear-editar_bolson_pendiente(32).html', objects=bolsones_pendientes, header=header,
                           features=features, first_dict=0)





#@admin_required
@bolson.route('/bolsones_previos')
def bolsones_previos():
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-previos',
        headers = headers,
        data = json.dumps(data))
    print(r.text)
    bolsones_previos = json.loads(r.text)['Bolsones Previos']
    header = "Lista de Bolsones Previos"
    url = "bolson.bolson_previo"
    ths_list = ["nombre", "estado"]
    return render_template('/bolson/Bolsones_previos_lista(11).html', objects = bolsones_previos, header = header ,url = url, ths_list = ths_list, first_dict = 0)


#@admin_required
@bolson.route('/bolson_previo/<int:id>')
def bolson_previo(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-previo/' + str(id),
        headers = headers)
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_previos'))
    bolson_previo = json.loads(r.text)
    header = "Bolsón Previo"
    return render_template('/bolson/Bolson_previo(12).html', object = bolson_previo, header = header)


#@admin_required
@bolson.route('/bolsones_en_venta')
def bolsones_en_venta():
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolsones-venta',
        headers = headers,
        data = json.dumps(data))
    print(r.text)
    bolsones_venta = json.loads(r.text)['Bolsones Venta']
    header = "Bolsones en Venta"
    url = "bolson.bolson_en_venta"
    feature = "nombre"
    return render_template('/bolson/Bolsones_venta(cliente)_lista(13).html', header = header, objects = bolsones_venta, url = url, feature = feature)
    #ths_list = ["nombre", "estado"]
    #return render_template('/bolson/Bolsones_venta(admin)_lista(15).html', objects = bolsones_venta, header = header ,url = url, ths_list = ths_list, first_dict = 0)

#@admin_required
@bolson.route('/bolson_en_venta/<int:id>')
def bolson_en_venta(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/bolson-venta/' + str(id),
        headers = headers)
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.bolsones_en_venta'))
    bolson_venta = json.loads(r.text)
    print(r.text)
    header = "Bolsón en Venta"
    return render_template('/bolson/Bolson_venta(cliente)(14).html', object = bolson_venta, header = header)


#@admin_required
@bolson.route('/productos')
def productos():
    data = {}
    #data['pagina'] = "1"
    #data['cantidad_elementos'] = "1"
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/productos',
        headers = headers,
        data = json.dumps(data))
    print(r.text)
    productos = json.loads(r.text)['Productos']
    header = 'Lista de Productos'
    url = 'bolson.producto'
    ths_list = ['nombre', 'id']
    return render_template('/bolson/Productos_lista(21).html', objects = productos, url = url, header = header, ths_list = ths_list, first_dict = 0)


#@admin_required
@bolson.route('/producto/<int:id>')
def producto(id):
    #auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " #+ auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/producto/' + str(id),
        headers = headers)
    if (r.status_code == 404) or (r.status_code == 400):
        return redirect(url_for('bolson.productos'))
    producto = json.loads(r.text)
    print(r.text)
    header = 'Producto'
    return render_template('/bolson/Producto(22).html', object = producto, header = header)



#@admin_required
@bolson.route('/crear_editar_producto')
def crear_editar_producto():
    data = {}
    # data['pagina'] = "1"
    # data['cantidad_elementos'] = "1"
    # auth = request.cookies['access_token']
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer "  # + auth
    }
    r = requests.get(
        current_app.config["API_URL"] + '/productos',
        headers=headers,
        data=json.dumps(data))
    print(r.text)
    productos = json.loads(r.text)['Productos']
    header = 'Crear/Editar Producto'
    features = ['nombre', 'usuario_ID']
    return render_template('/bolson/Crear-editar_producto(33).html', objects = productos, header = header, features = features, first_dict = 0)






