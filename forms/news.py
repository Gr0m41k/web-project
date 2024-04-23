from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    content = TextAreaField("Содержание", validators=[DataRequired()])
    submit = SubmitField('Применить')
