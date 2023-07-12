from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label="Nome de Usuário:")
    email_address = StringField(label="Email:")
    password1 = PasswordField(label="Senha:")
    password2 = PasswordField(label="Confirme a senha:")
    submit = SubmitField(label="Criar Conta")
