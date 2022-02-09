# - *- coding: utf- 8 - *-
from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField, SelectField, HiddenField, DateTimeField #Importa campos
from wtforms.fields.html5 import EmailField,DateField #Importa campos HTML
from wtforms import validators #Importa validaciones

class BolsonForm(FlaskForm):

    nombre = StringField('Nombre',
     [
         validators.required(message = 'Debe introducir un nombre'),
         validators.Length(min=5)
     ])

    estado = SelectField('Estado', choices = ['False', 'True'])


    fecha = DateTimeField('Fecha', format='%d/%m/%Y')


    submit = SubmitField('Guardar Información')


