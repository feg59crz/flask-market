from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    # se receber um form valido, adicionar user
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data,
                              )
        with app.app_context():
            db.session.add(user_to_create)
            db.session.commit()

            login_user(user_to_create)
            flash(f"Usuário criado com sucesso! Logado como {user_to_create.username}", category="success")
            return redirect(url_for('market_page'))
    # se existirem erros nos validators do registro
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Erro no registro de usuário: {err_msg[0]}", category="danger")

    return render_template("register.html", form=form)

@app.route("/login",  methods=["GET", "POST"])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        attemped_user = User.query.filter_by(username=form.username.data).first()
        if attemped_user and attemped_user.check_password_correction(attemped_password=form.password.data):
            login_user(attemped_user)
            flash(f"Sucesso! Logado como {attemped_user.username}.", category="success")
            return redirect(url_for("market_page"))
        else:
            flash("Usuário e/ou senha não válidos. Tente novamente", category="danger")

    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("Deslogado com sucesso.", category="info")
    return redirect(url_for("home_page"))