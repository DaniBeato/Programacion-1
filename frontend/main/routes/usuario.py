from flask import Blueprint,render_template

usuario = Blueprint('usuario', __name__, url_prefix = '/usuario')

@usuario.route('/administradores')
def administradores():
    return render_template('/usuario/Administradores_lista(4).html')

@usuario.route('/administrador')
def administrador():
    return render_template('/usuario/Administrador(5).html')

@usuario.route('/crear_editar_administrador')
def crear_editar_administrador():
    return render_template('/usuario/Crear-editar_administrador(36).html')

@usuario.route('/clientes')
def clientes():
    return render_template('/usuario/Clientes_lista(17).html')

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















