from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    dni = StringField('Dni', validators=[DataRequired()])
    submit = SubmitField('Guardar')
