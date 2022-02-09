# - *- coding: utf- 8 - *-
from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField, SelectField, HiddenField#Importa campos
from wtforms.fields.html5 import EmailField, DateTimeField #Importa campos HTML
from wtforms import validators #Importa validaciones


class FiltroForm(FlaskForm):
    nombre = StringField('Nombre', [validators.optional()])
    fecha = DateTimeField('Fecha', [validators.optional()], format='%Y', )
    estado = SelectField('Estado', [validators.optional()])
    submit = SubmitField("Filter")
