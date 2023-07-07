from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# dinamicaly routes - to receive some string after about page
@app.route("/about/<username>")
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'