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

    precio = StringField('Precio')

    producto = SelectField('Producto', coerce=int, validate_choice=False)

    producto2 = SelectField('Producto 2', coerce=int, validate_choice=False)

    producto3 = SelectField('Producto 3', coerce=int, validate_choice=False)

    producto4 = SelectField('Producto 4', coerce=int, validate_choice=False)

    submit = SubmitField('Guardar Información')


class BolsonFormEdit(FlaskForm):

    nombre = StringField('Nombre',
     [
         validators.required(message='Debe introducir un nombre'),
         validators.Length(min=5)
     ])

    estado = BooleanField()

    fecha = DateField('Fecha')

    submit = SubmitField('Guardar Información')

class BolsonFilter(FlaskForm):
    nombre = StringField('Nombre', [validators.optional()])
    estado = SelectField('Estado', [validators.optional()], choices=['', ('No aprobado'), ('Aprobado')])
    desde = DateField('Desde', [validators.optional()])
    hasta = DateField('Hasta', [validators.optional()])
    submit = SubmitField("Filtrar")


