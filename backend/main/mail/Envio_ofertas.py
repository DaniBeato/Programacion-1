from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuariosModels
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from main.mail.Funciones import enviar_ofertas, sendMail
from main.models import BolsonesModels
from datetime import  datetime, timedelta

fecha_vencimiento = datetime.today() - timedelta(days=7)


mail = Blueprint('mail', __name__, url_prefix = '/mail')
@mail.route('/envio_ofertas_resource', methods = ['POST'])
def envio_ofertas_resource():
    '''bolsones_venta = db.session.query(BolsonesModels).filter(BolsonesModels.fecha >= fecha_vencimiento).filter(BolsonesModels.estado == True)
    clientes = db.session.query(UsuariosModels).filter(UsuariosModels.rol == 'cliente')
    lista_mails = ([cliente.hacia_json().get('mail') for cliente in clientes])
    sent = enviar_ofertas(lista_mails, "¡Ofertas!", 'Ofertas', usuario = clientes)
    lista_mails = jsonify({'Destinatarios de las ofertas': lista_mails})
    return lista_mails, 201'''


    '''clientes = db.session.query(UsuariosModels).filter(UsuariosModels.rol == 'cliente')
    lista_usuarios = ([cliente.hacia_json() for cliente in clientes])
    for i in lista_usuarios:
        cliente = i.get('mail')
        sent = enviar_ofertas([cliente], "¡Ofertas!", 'Ofertas', usuario = cliente)
    lista_mails = ([cliente.hacia_json().get('mail') for cliente in clientes])
    lista_mails = jsonify({'Destinatarios de las ofertas': lista_mails})
    return lista_mails, 201'''



    '''clientes = db.session.query(UsuariosModels).filter(UsuariosModels.rol == 'Clientes')
    sent = enviar_ofertas([clientes], "¡Ofertas!", 'Ofertas', usuario = clientes)'''


    bolsones_venta = db.session.query(BolsonesModels).filter(BolsonesModels.fecha >= fecha_vencimiento).filter(BolsonesModels.estado == True)
    lista_bolsones_json = (bolson.hacia_json() for bolson in bolsones_venta)
    lista_bolsones_objetos = []
    for bolson in lista_bolsones_json:
        lista_bolsones_objetos.append(BolsonesModels.desde_json_ofertas(bolson))
    clientes = db.session.query(UsuariosModels).filter(UsuariosModels.rol == 'cliente')
    lista_clientes = ([cliente.hacia_json() for cliente in clientes])
    for cliente in lista_clientes:
        sent = enviar_ofertas([cliente.get('mail')], "¡Ofertas!", 'Ofertas', usuario = UsuariosModels.desde_json(cliente), bolsones_venta = lista_bolsones_objetos)
    lista_mails = jsonify({'Destinatarios de las ofertas': [cliente.hacia_json().get('mail') for cliente in clientes]})
    return lista_mails, 201







