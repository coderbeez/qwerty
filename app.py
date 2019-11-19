import os
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from forms import RegisterForm, LoginForm, NoteForm, LinkForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login" #WHERE: Corey Schafer Flask User Authentication
login_manager.login_message = u"Login for your notes!" #Flask Login documentation

def is_safe_url(next):
    if next.startswith("/notes/"):
        return True
    else:
        return False    


class User(UserMixin):
    def __init__(self, username, password, email, id):
        self.username = username
        self.password = password
        self.email = email
        self.id = id

    @staticmethod
    def get_user(email):
        user = mongo.db.users.find_one({"email": email})
        return User(user['user_name'], user['password'], user['email'], user['_id'])

    @staticmethod
    def get_user_by_id(id):
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        return User(user['user_name'], user['password'], user['email'], user['_id'])


@login_manager.user_loader
def load_user(id):
    u = User.get_user_by_id(id)
    if not u:
        return None
    return u
    #WHERE: How to use MongoDB (and PyMongo) with Flask-Login https://boh717.github.io/post/flask-login-and-mongodb/ & Corey


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_email = mongo.db.users.find_one({"email": form.email.data})
        #WHERE: Pretty Printed 
        if existing_email:
            flash("Oops email exists - check email or select note language to login!", "error")

        else: 
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            #WHERE: Corey Schafer Flask User Authentication https://www.youtube.com/watch?v=CSHx6eCkmv0&t=1052s
            mongo.db.users.insert_one({"user_name": form.name.data, "email": form.email.data, "password": hashed_password })
            user = User.get_user(form.email.data)
            login_user(user)
            flash("Perfect - select note language!")
            return redirect(url_for('index'))

    return render_template("register.html", form=form)

#LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user(form.email.data)
        print(user.username)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Perfect - your notes!")
            next = request.args.get("next") #WHAT: getting the argument from the url
            print(f'next text {next}')
            if not is_safe_url(next): #WHAT: making sure the checking the redirect is safe
                return abort(400)
            return redirect(next or url_for('index'))
            #WHERE: Flask Login documentation  
        else:
            flash("Oops - check email & password!", "error")    
    return render_template("login.html", form=form)


#VIEW LINKS
@app.route("/links/<language>", methods=["GET", "POST"])
def links(language):
    links = list(mongo.db.links.find({"language": language}).sort([("topic", 1),("link_type", 1),("link_name", 1)]))
    #create array from cursor returned
    group_topics = mongo.db.links.aggregate([ {"$match": {"language": language }}, {"$group":{"_id" :"$topic"}}, {"$sort": { "_id": 1}}])
    group_topics = list(group_topics)
    #change from cursor to array
    return render_template("links.html", links=links, group_topics=group_topics, language=language)


#VIEW NOTES
@app.route("/notes/<language>")
@login_required
def notes(language):
    print(current_user.id)
    notes = list(mongo.db.notes.find({"language": language, "user_id": ObjectId(current_user.id)}).sort([("topic", 1),("note_name", 1)]))
    #create array from cursor returned
    print(len(notes))
    group_topics = mongo.db.notes.aggregate([ {"$match": {"language": language, "user_id": ObjectId(current_user.id) }}, {"$group":{"_id" :"$topic"}}, {"$sort": { "_id": 1}}])
    group_topics = list(group_topics)
    #print(group_topics)
    #change from cursor to array
    return render_template("notes.html", notes=notes, group_topics=group_topics, language=language)


#ADD LINK
@app.route("/addlink/<language>", methods=["GET", "POST"])
def addlink(language):
    form = LinkForm()
    document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
    topics = document_language["topics"]
    form.topic.choices = [("", "-select-")]+[(topic, topic) for topic in topics] #slugify?
    #WHERE: https://stackoverflow.com/questions/40905579/flask-wtf-dynamic-select-field-with-an-empty-option
    #WHERE: https://stackoverflow.com/questions/28133859/how-to-populate-wtform-select-field-using-mongokit-pymongo
    #print(topics)
    #print(form.topic.choices)
    if form.validate_on_submit():
        existing_link = mongo.db.links.find_one({"language": language, "url": form.url.data})
        #in case its vaid to have the link in multiple languages... want to only search current language
        #WHERE: Pretty Printed

        if existing_link:
            print(existing_link["_id"])
            mongo.db.links.update_one({"_id": ObjectId(existing_link["_id"])},{"$push": {"ratings": int(form.rate.data)}})
            flash(f'Link exists: {existing_link["topic"]} - {existing_link["link_type"]} - {existing_link["link_name"]}. Your rating was added!')
            return redirect(url_for("links", language=language))
        else:    
            mongo.db.links.insert_one({"language": language, "topic": form.topic.data, "url": form.url.data, "link_name": form.name.data, "link_type": form.link_type.data, "description": form.description.data, "ratings": [int(form.rate.data)] })
            flash("Perfect - link added!")
            return redirect(url_for("links", language=language))
                       
    #else:
        #flash("Oops - check fields!", "error")
    return render_template("addlink.html", form=form, language=language) 


#ADD_NOTE
@app.route("/addnote/<language>", methods=["GET", "POST"])
@login_required
def addnote(language):
    form = NoteForm()
    document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
    topics = document_language["topics"]
    form.topic.choices = [("", "-select-")]+[(topic, topic) for topic in topics] #slugify?
    print(topics)
    print(form.topic.choices)
    if form.validate_on_submit():
        mongo.db.notes.insert_one({"user_id": ObjectId("5db5cc531c9d440000690ae2"), "language": language, "topic": form.topic.data, "note_name": form.name.data, "content": form.content.data })
        flash("Perfect - note added!")
        return redirect(url_for("notes", language=language))
    elif request.method == "GET":
        pass    
    else:
        flash("Oops - check fields!", "error")
    return render_template("addnote.html", form=form, language=language)


#EDIT_NOTE
@app.route("/editnote/<language>/<noteid>", methods=["GET", "POST"])
@login_required
def editnote(language, noteid):
    note = mongo.db.notes.find_one_or_404({"_id": ObjectId(noteid)})
    #no list as want to return single object
    form = NoteForm()
    document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
    topics = document_language["topics"]
    form.topic.choices = [("", "-select-")]+[(topic, topic) for topic in topics]
    if form.validate_on_submit():
        print("valid")
        mongo.db.notes.update_one({"_id": ObjectId(noteid)},{"$set": {"topic": form.topic.data, "note_name": form.name.data ,"content": form.content.data}})
        #using note.update_one throws an error???
        flash("Perfect - note updated!")
        return redirect(url_for("notes", language=language))
    elif request.method == "GET":
        form.topic.data = note["topic"]
        form.name.data = note["note_name"]
        form.content.data = note["content"]
    else:
        flash("Oops - check fields!", "error") 
    print(note)    
    return render_template("editnote.html", form=form, note=note, language=language)


#DELETE_NOTE
@app.route("/deletenote/<language>/<noteid>", methods=["GET","POST"]) #just post???
@login_required
def deletenote(language, noteid):
    note = mongo.db.notes.find_one_or_404({"_id": ObjectId(noteid)})
    #no list as want to return single object
    mongo.db.notes.delete_one({"_id": ObjectId(noteid)})
    flash("Perfect - note deleted!") 
    return redirect(url_for("notes", language=language))


#FLAG LINK    
@app.route("/flaglink/<language>/<linkid>", methods=["POST"])
def flaglink(language, linkid):
    link = mongo.db.links.find_one_or_404({"_id": ObjectId(linkid)})
    #no list as want to return single object
    mongo.db.links.update_one({"_id": ObjectId(linkid)},{"$set": {"flag": True}})
    flash("Perfect - link flagged!") 
    return redirect(url_for("links", language=language))


#RATE LINK
@app.route("/ratelink/<language>/<linkid>/<rating>", methods=["POST"])
def ratelink(language, linkid, rating):
    link = mongo.db.links.find_one_or_404({"_id": ObjectId(linkid)})
    #no list as want to return single object
    mongo.db.links.update_one({"_id": ObjectId(linkid)},{"$push": {"ratings": int(rating)}})
    flash("Perfect - link rated!") 
    return redirect(url_for("links", language=language))  


#LOGOUT
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Perfect - logged out!") 
    return redirect(url_for("index")) 
    #WHERE: Flask Login documentation https://flask-login.readthedocs.io/en/latest/

    
       



if __name__ == '__main__':
    app.run(debug=True)