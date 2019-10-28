from flask import Flask, render_template, url_for
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')




@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/notes")
def notes():
    return render_template('notes.html')


@app.route("/addnote")
def addnote():
    return render_template('addnote.html')


@app.route("/editnote")
def editnote():
    return render_template('editnote.html')


@app.route("/links")
def links():
    return render_template('links.html')


@app.route("/addlink")
def addlink():
    return render_template('addlink.html') 


if __name__ == '__main__':
    app.run(debug=True)