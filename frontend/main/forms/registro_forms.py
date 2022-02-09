# - *- coding: utf- 8 - *-
from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField, SelectField, HiddenField #Importa campos
from wtforms.fields.html5 import EmailField,DateField #Importa campos HTML
from wtforms import validators #Importa validaciones

class RegistroForm(FlaskForm):

    nombre = StringField('Nombre',
     [
         validators.required(message = 'Debe introducir un nombre'),
         validators.Length(min=5)
     ])

    apellido = StringField('Apellido',
    [
         validators.required(message='Debe introducir un apellido'),
         validators.Length(min=5)
    ])

    email = EmailField('E-mail',
    [
        validators.Required(message="Debe introducir un email"),
        validators.Email(message='Formato inválido'),
        ])


    telefono = StringField('Teléfono',
    [
     validators.Required(message="Debe introducir un teléfono"),
     #validators.Required(message="Formato inválido")
    ])


    contrasenia = StringField('Contraseña',
    [
        validators.required(message='Debe introducir una contraseña'),
        validators.Length(min=3)
    ])

    rol = SelectField('Rol', choices = ['admin', 'cliente', 'proveedor'])

    submit = SubmitField('Guardar Información')

    fields = ['nombre', 'apellido', 'email', 'telefono', 'contrasenia', 'rol']

