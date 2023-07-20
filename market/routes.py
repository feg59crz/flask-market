from market import app, db
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market", methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()

    if request.method == "POST":
        purchased_item = request.form.get("purchased_item")
        p_item_obj = Item.query.filter_by(name=purchased_item).first()
        if p_item_obj:
            if current_user.can_purchase(p_item_obj):
                p_item_obj.buy(current_user)
                flash(f"Você comprou o '{p_item_obj.name}' por R$ {p_item_obj.price}!", category="success")
            else:
                flash(f"Compra não realizada. Não há recursos suficientes para comprar '{p_item_obj.name}'", category="danger")
        
        return redirect(url_for("market_page"))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items)

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