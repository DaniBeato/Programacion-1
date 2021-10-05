from flask import Blueprint, render_template

bolson = Blueprint('bolson', __name__, url_prefix = '/bolson')

@bolson.route('/bolsones')
def bolsones():
    return render_template('/bolson/Bolsones_lista(7).html')

@bolson.route('/bolson')
def bolson_():
    return render_template('/bolson/Bolson(8).html')

@bolson.route('/bolsones_pendientes')
def bolsones_pendientes():
    return render_template('/bolson/Bolsones_pendientes_lista(9).html')

@bolson.route('/bolson_pendiente')
def bolson_pendiente():
    return render_template('/bolson/Bolson_pendiente(10).html')

@bolson.route('/crear_editar_bolson_pendiente')
def crear_editar_bolson_pendiente():
    return render_template('/bolson/Crear-editar_bolson_pendiente(32).html')

@bolson.route('/bolsones_previos')
def bolsones_previos():
    return render_template('/bolson/Bolsones_previos_lista(11).html')

@bolson.route('/bolson_previo')
def bolson_previo():
    return render_template('/bolson/Bolson_previo(12).html')

@bolson.route('/bolsones_en_venta')
def bolsones_en_venta():
    return render_template('/bolson/Bolsones_venta(cliente)_lista(13).html')

@bolson.route('/bolson_en_venta')
def bolson_en_venta():
    return render_template('/bolson/Bolson_venta(cliente)(14).html')

@bolson.route('/productos')
def productos():
    return render_template('/bolson/Productos_lista(21).html')

@bolson.route('/producto')
def producto():
    return render_template('/bolson/Producto(22).html')

@bolson.route('/crear_editar_producto')
def crear_editar_producto():
    return render_template('/bolson/Crear-editar_producto(33).html')




