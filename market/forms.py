from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from market import app
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Nome de usuário já existe! Tente outro nome de usuário.')
        
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email já registrado!')
        
    username = StringField(label="Nome de Usuário:", validators=[
        Length(min=3, max=30, message="Nome de usuário deve ter entre 3 e 30 caracteres"), 
        DataRequired()]) # [] - lista de validators
    
    email_address = StringField(label="Email:", validators=[Email(message="Email inválido"), DataRequired()])
    
    password1 = PasswordField(label="Senha:", validators=[
        Length(min=6, message="Senha deve ser maior que 6 caracteres"), DataRequired()])
    
    password2 = PasswordField(label="Confirme a senha:", validators=[
        EqualTo('password1', message="Senhas devem ser iguais"), DataRequired()]) # EqualTo - compara as senhas
    
    submit = SubmitField(label="Criar Conta")

class LoginForm(FlaskForm):
    username = StringField(
        label="Usuário:",
        validators=[DataRequired()]
    )
    password = PasswordField(
        label="Senha:",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Acessar")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Comprar Item")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Vender Item")
