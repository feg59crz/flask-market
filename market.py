from flask import Flask, render_template

app = Flask(__name__)

# using templates
@app.route('/')
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = [
        {"id": 1, "name": "Phone", "barcode": "8932546468", "price": 500},
        {"id": 2, "name": "Laptop", "barcode": "8932530945", "price": 900},
        {"id": 3, "name": "Keyboard", "barcode": "8932523467", "price": 150},
    ]
    return render_template('market.html', items=items)