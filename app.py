import os
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import RegisterForm, LoginForm, NoteForm, LinkForm


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


@app.route("/links/<language>", methods=["GET", "POST"])
def links(language):
    links = list(mongo.db.links.find({"language": language}).sort([("topic", 1),("link_type", 1),("link_name", 1)]))
    #create array from cursor returned
    group_topics = mongo.db.links.aggregate([ {"$match": {"language": language }}, {"$group":{"_id" :"$topic"}}, {"$sort": { "_id": 1}}])
    group_topics = list(group_topics)
    #change from cursor to array
    return render_template("links.html", links=links, group_topics=group_topics, language=language)


@app.route("/notes/<language>")
def notes(language):
    notes = list(mongo.db.notes.find({"language": language }).sort([("topic", 1),("note_name", 1)]))
    #create array from cursor returned
    group_topics = mongo.db.notes.aggregate([ {"$match": {"language": language }}, {"$group":{"_id" :"$topic"}}, {"$sort": { "_id": 1}}])
    group_topics = list(group_topics)
    print(group_topics)
    #change from cursor to array
    return render_template("notes.html", notes=notes, group_topics=group_topics, language=language)


@app.route("/addlink/<language>", methods=["GET", "POST"])
def addlink(language):
    form = LinkForm()
    document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
    topics = document_language["topics"]
    form.topic.choices = [(topic, topic) for topic in topics] #slugify?
    print(topics)
    print(form.topic.choices)
    if form.validate_on_submit():
        #flash("Perfect - link added!")
        mongo.db.links.insert_one({"language": language, "topic": form.topic.data, "url": form.url.data, "link_name": form.name.data, "link_type": form.link_type.data, "description": form.description.data, "ratings": [int(form.rate.data)] })
        flash("Perfect - link added!")
        return redirect(url_for("links", language=language))
    #else:
        #flash("Oops - try again")
    return render_template("addlink.html", form=form, language=language) 


@app.route("/addnote/<language>", methods=["GET", "POST"])
def addnote(language):
    form = NoteForm()
    document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
    topics = document_language["topics"]
    form.topic.choices = [(topic, topic) for topic in topics] #slugify?
    ##WHERE: https://stackoverflow.com/questions/28133859/how-to-populate-wtform-select-field-using-mongokit-pymongo
    print(topics)
    print(form.topic.choices)
    if form.validate_on_submit():
        mongo.db.notes.insert_one({"user_id": ObjectId("5db5cc531c9d440000690ae2"), "language": language, "topic": form.topic.data, "note_name": form.name.data, "content": form.content.data })
        flash("Perfect - note added!")
        return redirect(url_for("notes", language=language))
    elif request.method == "GET":
        pass    
    else:
        flash("Oops - try again")
    return render_template("addnote.html", form=form, language=language)


@app.route("/editnote/<language>/<noteid>", methods=["GET", "POST"])
def editnote(language, noteid):
    note = mongo.db.notes.find_one_or_404({"_id": ObjectId(noteid)})
    print(note)
    #no list as want to return single object
    form = NoteForm()
    if form.validate_on_submit():
        print("valid")
        mongo.db.notes.update_one({"_id": ObjectId(noteid)},{"$set": {"topic": form.topic.data, "note_name": form.name.data ,"content": form.content.data}})
        #using note.update_one throws an error???
        flash("Perfect - note updated!")
        return redirect(url_for("notes", language=language))
    elif request.method == "GET":
        #form.language.data = note["language"]
        form.topic.data = note["topic"]
        form.name.data = note["note_name"]
        form.content.data = note["content"]
    else:
        flash("Oops - try again") 
    return render_template("editnote.html", form=form, note=note, language=language)


@app.route("/deletenote/<language>/<noteid>", methods=["GET","POST"]) #just post???
def deletenote(language, noteid):
    note = mongo.db.notes.find_one_or_404({"_id": ObjectId(noteid)})
    #no list as want to return single object
    mongo.db.notes.delete_one({"_id": ObjectId(noteid)})
    flash("Post deleted") 
    return redirect(url_for("notes", language=language))
    
@app.route("/flaglink/<language>/<linkid>", methods=["POST"])
def flaglink(language, linkid):
    link = mongo.db.links.find_one_or_404({"_id": ObjectId(linkid)})
    #no list as want to return single object
    mongo.db.links.update_one({"_id": ObjectId(linkid)},{"$set": {"flag": True}})
    flash("Link flagged") 
    return redirect(url_for("links", language=language))


@app.route("/ratelink/<language>/<linkid>/<rating>", methods=["POST"])
def ratelink(language, linkid, rating):
    link = mongo.db.links.find_one_or_404({"_id": ObjectId(linkid)})
    #no list as want to return single object
    mongo.db.links.update_one({"_id": ObjectId(linkid)},{"$push": {"ratings": int(rating)}})
    flash("Link rated") 
    return redirect(url_for("links", language=language))  

    
       



if __name__ == '__main__':
    app.run(debug=True)