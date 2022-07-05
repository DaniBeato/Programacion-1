# - *- coding: utf- 8 - *-
from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField, IntegerField, SelectField, HiddenField, DateField,BooleanField #Importa campos
from wtforms.fields.html5 import EmailField,DateField #Importa campos HTML
from wtforms import validators #Importa validaciones

class ProductoForm(FlaskForm):

    nombre = StringField('Nombre',
     [
         validators.required(message = 'Debe introducir un nombre'),
     ])

    usuario_ID = SelectField()


    submit = SubmitField('Guardar Información')


class ProductoFilter(FlaskForm):
    nombre = StringField('Nombre', [validators.optional()])
    submit = SubmitField("Filtrar")
