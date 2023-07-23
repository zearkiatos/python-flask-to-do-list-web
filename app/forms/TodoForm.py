from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')