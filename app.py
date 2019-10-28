from flask import Flask, render_template, url_for
from forms import RegisterForm, LoginForm, AddNoteForm, AddLinkForm
import os


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/register")
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form )


@app.route("/notes")
def notes():
    return render_template('notes.html')


@app.route("/addnote")
def addnote():
    form = AddNoteForm()
    return render_template('addnote.html', form=form)


@app.route("/editnote")
def editnote():
    return render_template('editnote.html')


@app.route("/links")
def links():
    return render_template('links.html')


@app.route("/addlink")
def addlink():
    form = AddLinkForm()
    return render_template('addlink.html', form=form) 


if __name__ == '__main__':
    app.run(debug=True)