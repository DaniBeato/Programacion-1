# - *- coding: utf- 8 - *-
from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField #Importa campos
from wtforms.fields.html5 import EmailField,DateField #Importa campos HTML
from wtforms import validators #Importa validaciones

class IngresoForm(FlaskForm):

    mail = EmailField('Mail',
        [
            validators.Required(message="Debe introducir un mail"),
            validators.Email(message='Formato inválido'),
        ])

    contrasenia = PasswordField('Contraseña',
        [
            validators.required(message='Debe introducir una contraseña'),
            validators.Length(min=3)
        ])

    submit = SubmitField('Ingresar')
