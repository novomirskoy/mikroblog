from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired


class CreatePostForm(Form):
    name = StringField('Заголовок', validators=[DataRequired()])
    text = TextAreaField('Текст', validators=[DataRequired()])


class LoginForm(Form):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])