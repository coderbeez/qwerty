from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm, AddNoteForm, AddLinkForm
import os
import pymongo


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

MONGODB_URI = os.getenv("MONGO_URI")
DB = "qwerty"
COLL_USER = "user"
COLL_LANGUAGE = "language"
COLL_NOTE = "note"
COLL_LINK = "link"

def mongo_connect(uri):
    try:
        connect = pymongo.MongoClient(uri)
        print("Mongo is connected!")
        return connect
    except pymongo.errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}") 

mongo_connect(MONGODB_URI)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash("Perfect - you can create notes!")
        return redirect(url_for("addnote"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "edel@test.com" and form.password.data == "123456789":
            #temp till authentication setup
            flash("Perfect - your notes!")
            return redirect(url_for("notes"))
        else:
            flash("Oops - try again")    
    return render_template("login.html", form=form )


@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/addnote", methods=["GET", "POST"])
def addnote():
    form = AddNoteForm()
    if form.validate_on_submit():
        flash("Perfect - note added!")
        return redirect(url_for("notes"))
    return render_template("addnote.html", form=form)


@app.route("/editnote", methods=["GET", "POST"])
def editnote():
    return render_template("editnote.html")


@app.route("/links", methods=["GET", "POST"])
def links():
    return render_template("links.html")


@app.route("/addlink", methods=["GET", "POST"])
def addlink():
    form = AddLinkForm()
    if form.validate_on_submit():
        #flash("Perfect - link added!")
        return redirect(url_for("links"))
    else:
        flash("Oops - try again")
    return render_template("addlink.html", form=form) 


if __name__ == '__main__':
    app.run(debug=True)