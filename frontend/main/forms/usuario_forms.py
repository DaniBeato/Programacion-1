# - *- coding: utf- 8 - *-
from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField, SelectField, HiddenField, DateField #Importa campos
from wtforms.fields.html5 import EmailField,DateField #Importa campos HTML
from wtforms import validators #Importa validaciones

class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre',
     [
         validators.required(message='Debe introducir un nombre'),
         validators.Length(min=2)
     ])

    apellido = StringField('Apellido',
    [
       validators.required(message='Debe introducir un apellido'),
       validators.Length(min=2)
    ])

    email = EmailField('E-mail',
    [
       validators.Required(message="Debe introducir un email"),
       validators.Email(message='Formato inválido'),
    ])

    telefono = StringField('Teléfono',
    [
       validators.Required(message="Debe introducir un teléfono"),
       # validators.Required(message="Formato inválido")
    ])

    contrasenia = PasswordField('Contraseña',
    [
        validators.required(message='Debe introducir una contraseña'),
        validators.Length(min=3)
    ])


    rol = SelectField('Rol', choices=['admin', 'cliente', 'proveedor'])

    submit = SubmitField('Guardar Información')


class UsuarioFilter(FlaskForm):
    nombre = StringField('Nombre', [validators.optional()])
    apellido = StringField('Apellido', [validators.optional()])
    submit = SubmitField("Filtrar")

