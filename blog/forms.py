from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired


class CreatePostForm(Form):
	name = TextField('Заголовок', validators=[DataRequired()])
	text = TextAreaField('Текст', validators=[DataRequired()])