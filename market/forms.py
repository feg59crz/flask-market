from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

"""
flask_wtf, wtforms - Formulários
validators - conferem os dados
"""
class RegisterForm(FlaskForm):
    username = StringField(label="Nome de Usuário:", validators=[Length(min=3, max=30, message="Nome de usuário deve ter entre 3 e 30 caracteres"), DataRequired()]) # [] - lista de validators
    email_address = StringField(label="Email:", validators=[Email(message="Email inválido"), DataRequired()])
    password1 = PasswordField(label="Senha:", validators=[Length(min=6, message="Senha deve ser maior que 6 caracteres"), DataRequired()])
    password2 = PasswordField(label="Confirme a senha:", validators=[EqualTo('password1', message="Senhas devem ser iguais"), DataRequired()]) # EqualTo - compara as senhas
    submit = SubmitField(label="Criar Conta")
