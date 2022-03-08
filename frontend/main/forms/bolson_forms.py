# - *- coding: utf- 8 - *-
from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField, SelectField, HiddenField, DateField, BooleanField #Importa campos
from wtforms.fields.html5 import EmailField, DateField #Importa campos HTML
from wtforms import validators #Importa validaciones

class BolsonForm(FlaskForm):

    nombre = StringField('Nombre',
     [
         validators.required(message = 'Debe introducir un nombre'),
         validators.Length(min=5)
     ])

    estado = BooleanField()


    fecha = DateField('Fecha')


    submit = SubmitField('Guardar Información')


class BolsonFilter(FlaskForm):
    nombre = StringField('Nombre', [validators.optional()])
    estado = SelectField('Estado', [validators.optional()], choices=['', (0), (1)])
    desde = DateField('Desde', [validators.optional()])
    hasta = DateField('Hasta', [validators.optional()])
    submit = SubmitField("Filtrar")


