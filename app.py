import os
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.son import SON
from forms import RegisterForm, LoginForm, AddNoteForm, AddLinkForm


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)



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
    notes = list(mongo.db.notes.find({"language": "Python"}).sort([("topic", 1),("note_name", 1)]))
    #create array from cursor returned
    group_topics = mongo.db.notes.aggregate([ {"$match": {"language": "Python"}}, {"$sort": SON([("topic", -1)])},{"$group":{"_id" :"$topic"}}, ])
    group_topics = list(group_topics)
    #change from cursor to array
    return render_template("notes.html", notes=notes, group_topics=group_topics )


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
    links = list(mongo.db.links.find({"language": "Python"}).sort([("topic", 1),("link_type", 1),("link_name", 1)]))
    #create array from cursor returned
    group_topics = mongo.db.links.aggregate([{"$match": {"language": "Python"}}, {"$sort": SON([("topic", -1)])},{"$group":{"_id" :"$topic"}}])
    group_topics = list(group_topics)
    #change from cursor to array
    return render_template("links.html", links=links, group_topics=group_topics)


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