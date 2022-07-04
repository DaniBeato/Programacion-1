# - *- coding: utf- 8 - *-
from flask_wtf import FlaskForm #Importa funciones de formulario
from wtforms import PasswordField, SubmitField, StringField, SelectField, HiddenField, IntegerField, DateField, BooleanField #Importa campos
from wtforms.fields.html5 import EmailField,DateField #Importa campos HTML
from wtforms import validators #Importa validaciones


class CompraForm(FlaskForm):

    usuario_ID = IntegerField('Usuario_ID')

    bolsonID = IntegerField('BolsonID')

    retirado = BooleanField('Retirado')

    fecha_compra = DateField('Fecha')


    submit = SubmitField('Guardar Información')



class CompraFilter(FlaskForm):
    usuario_ID = IntegerField('Usuario_ID', [validators.optional()])
    retirado = SelectField('Retirado', [validators.optional()], choices=[(''), ('No'), ('Sí')])
    submit = SubmitField("Filtrar")


