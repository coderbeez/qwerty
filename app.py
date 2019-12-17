import os
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from forms import RegisterForm, LoginForm, NoteForm, LinkForm, SearchForm
from time import sleep


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)
bcrypt = Bcrypt(app)


#LOGIN MANAGER
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = u"Login for your notes!"


#SAFE URL FOR LOGIN MANAGER
def is_safe_url(next):
    if next.startswith("/notes/"):
        return True
    else:
        return False    


#USER CLASS FOR LOGIN MANAGER
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


#LOAD USER FOR LOGIN MANAGER
@login_manager.user_loader
def load_user(id):
    u = User.get_user_by_id(id)
    if not u:
        return None
    return u


#WHERE: Login Manager approach melting pot of:
# Flask Login documentation
# Corey Schafer Flask User Authentication https://www.youtube.com/watch?v=CSHx6eCkmv0&t=1052s
# Corey Schafer Classes 
# Printy Printed 
# How to use MongoDB (and PyMongo) with Flask-Login https://boh717.github.io/post/flask-login-and-mongodb/


#HOME
@app.route("/")
@app.route("/index")
def index():  
    global sample1
    global sample2
    global sample3
    global sample4
    global quote
    sample1 = list(mongo.db.links.aggregate([{"$match": {"language": "HTML", "check": True, "flag": False}}, {"$sample": {"size": 1}}, {"$project":{"language": 1, "link_name": 1, "url": 1, "_id": 0}}]))[0]
    sample2 = list(mongo.db.links.aggregate([{"$match": {"language": "CSS", "check": True, "flag": False}}, {"$sample": {"size": 1}}, {"$project":{"language": 1, "link_name": 1, "url": 1, "_id": 0}}]))[0]
    sample3 = list(mongo.db.links.aggregate([{"$match": {"language": "JavaScript", "check": True}}, {"$sample": {"size": 1}}, {"$project":{"language": 1, "link_name": 1, "url": 1, "_id": 0}}]))[0]
    sample4 = list(mongo.db.links.aggregate([{"$match": {"language": "Python", "check": True, "flag": False}}, {"$sample": {"size": 1}}, {"$project":{"language": 1, "link_name": 1, "url": 1, "_id": 0}}]))[0]
    quote = list(mongo.db.quotes.aggregate([{"$sample": {"size": 1}}, {"$project":{"quote": 1, "author": 1, "_id": 0}}]))[0]
    return render_template("index.html", sample1=sample1, sample2=sample2, sample3=sample3, sample4=sample4, quote=quote)
#WHERE: Global variables from https://www.geeksforgeeks.org/global-local-variables-python/


#REGISTER - allows a user register for notes using unique email and hashed password.
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_email = mongo.db.users.find_one({"email": form.email.data})
        if existing_email:
            flash("Oops email exists - check email or select note language to login!", "error")
        else: 
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            mongo.db.users.insert_one({"user_name": form.name.data, "email": form.email.data, "password": hashed_password })
            user = User.get_user(form.email.data)
            login_user(user)
            flash("Perfect - select a notes language!")
            return redirect(url_for('index'))
    elif request.method == "GET":
        pass                    
    else:
        flash("Oops - check fields!", "error")      
    return render_template("register.html", form=form, sample1=sample1, sample2=sample2, sample3=sample3, sample4=sample4, quote=quote)
#WHERE: Hashing passwords from Corey Schafer Flask User Authentication https://www.youtube.com/watch?v=CSHx6eCkmv0&t=1052s


#LOGIN - allows a user log in to access their notes using email and password.
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user(form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Perfect - your notes!")
            next = request.args.get("next")
            if not is_safe_url(next):
                return abort(400)
            return redirect(next or url_for('index'))             
        else:
            flash("Oops - check email & password!", "error")
    elif request.method == "GET":
        pass                    
    else:
        flash("Oops - check fields!", "error")        
    return render_template("login.html", form=form, sample1=sample1, sample2=sample2, sample3=sample3, sample4=sample4, quote=quote)


#VIEW LINKS - allows all users to view and search links.
@app.route("/links/<language>", methods=["GET", "POST"])
def links(language):  
    links = list(mongo.db.links.find({"language": language}).sort([("topic", 1),("link_type", 1),("link_name", 1)]))
    group_topics = mongo.db.links.aggregate([ {"$match": {"language": language }}, {"$group":{"_id" :"$topic"}}, {"$sort": { "_id": 1}}])
    form = SearchForm()
    if form.validate_on_submit():
        mongo.db.links.create_index([("$**", "text")], language_override="en")
        links_search = list(mongo.db.links.find({"language": language, "$text": {"$search": form.tsearch.data}}).sort([("topic", 1),("link_type", 1),("link_name", 1)]))
        if links_search == []:
            flash(f'Sorry no results for {form.tsearch.data}', 'search')
        else:
            links = links_search
            group_topics = mongo.db.links.aggregate([ {"$match": {"language": language, "$text": {"$search": form.tsearch.data} }}, {"$group":{"_id" :"$topic"}}, {"$sort": { "_id": 1}}])
            flash(f'Links filtered by {form.tsearch.data}', 'search')    
    group_topics = list(group_topics)
    return render_template("links.html", links=links, group_topics=group_topics, language=language, form=form, sample1=sample1, sample2=sample2, sample3=sample3, sample4=sample4, quote=quote)
#WHERE: Text search from https://stackoverflow.com/questions/48371016/pymongo-how-to-use-full-text-search
# and https://stackoverflow.com/questions/50071593/pymongo-language-override-unsupported-c-when-creating-index


#VIEW NOTES - allows a user view and search their own notes for a language.
# Creates values for a language/user specific topic list.
@app.route("/notes/<language>", methods=["GET", "POST"] )
@login_required
def notes(language):
    notes = list(mongo.db.notes.find({"language": language, "user_id": ObjectId(current_user.id)}).sort([("topic", 1),("note_name", 1)]))
    if notes == []:
        flash(f'Click Add New + to add your first {language} note.', 'first')  
    group_topics = mongo.db.notes.aggregate([ {"$match": {"language": language, "user_id": ObjectId(current_user.id) }}, {"$group":{"_id" :"$topic"}}, {"$sort": { "_id": 1}}])
    form = SearchForm()
    if form.validate_on_submit():
        mongo.db.notes.create_index([("$**", "text")], language_override="en")
        notes_search = list(mongo.db.notes.find({"language": language, "user_id": ObjectId(current_user.id), "$text": {"$search": form.tsearch.data}}).sort([("topic", 1),("note_name", 1)]))
        if notes_search == []:
            flash(f'Sorry no results for {form.tsearch.data}', 'search')
        else:
            notes = notes_search
            group_topics = mongo.db.notes.aggregate([ {"$match": {"language": language, "user_id": ObjectId(current_user.id), "$text": {"$search": form.tsearch.data} }}, {"$group":{"_id" :"$topic"}}, {"$sort": { "_id": 1}}])
            flash(f'Notes filtered by {form.tsearch.data}', 'search')        
    group_topics = list(group_topics)    
    return render_template("notes.html", notes=notes, group_topics=group_topics, language=language, form=form, sample1=sample1, sample2=sample2, sample3=sample3, sample4=sample4, quote=quote)
#WHERE: Text search from https://stackoverflow.com/questions/48371016/pymongo-how-to-use-full-text-search
# and https://stackoverflow.com/questions/50071593/pymongo-language-override-unsupported-c-when-creating-index


#ADD LINK - allows a user add a new link for a language or a rating for an existing language link.
#Creates values for a language specific topic select field.
@app.route("/addlink/<language>", methods=["GET", "POST"])
def addlink(language):
    form = LinkForm()
    document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
    topics = document_language["topics"]
    form.topic.choices = [("", "-select-")]+[(topic, topic) for topic in topics]    
    if form.validate_on_submit():
        existing_link = mongo.db.links.find_one({"language": language, "url": form.url.data})
        if existing_link:
            print(existing_link["_id"])
            mongo.db.links.update_one({"_id": ObjectId(existing_link["_id"])},{"$push": {"ratings": int(form.rate.data)}})
            flash(f'Link exists: {existing_link["topic"]} - {existing_link["link_type"]} - {existing_link["link_name"]}. Your rating was added!')
            return redirect(url_for("links", language=language))
        else:    
            mongo.db.links.insert_one({"language": language, "topic": form.topic.data, "url": form.url.data, "link_name": form.name.data, "link_type": form.link_type.data, "description": form.description.data, "check": True, "flag": False,"ratings": [int(form.rate.data)] })
            #PRODUCTION SET CHECK TO FALSE!!!
            flash("Perfect - link added!")
            return redirect(url_for("links", language=language))
    elif request.method == "GET":
        pass                    
    else:
        flash("Oops - check fields!", "error")
    return render_template("addlink.html", form=form, language=language, sample1=sample1, sample2=sample2, sample3=sample3, sample4=sample4, quote=quote) 
#WHERE: Topics select field code from https://stackoverflow.com/questions/40905579/flask-wtf-dynamic-select-field-with-an-empty-option
# and https://stackoverflow.com/questions/28133859/how-to-populate-wtform-select-field-using-mongokit-pymongo
#WHY: Existing link check - as its valid to have the link in multiple languages, in this case only want to search current language.


#ADD_NOTE - allows a user add a note for a language. Creates values for a language specific topic select field.
@app.route("/addnote/<language>", methods=["GET", "POST"])
@login_required
def addnote(language):
    form = NoteForm()
    document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
    topics = document_language["topics"]
    form.topic.choices = [("", "-select-")]+[(topic, topic) for topic in topics]
    if form.validate_on_submit():
        mongo.db.notes.insert_one({"user_id": ObjectId(current_user.id), "language": language, "topic": form.topic.data, "note_name": form.name.data, "content": form.content.data })
        flash("Perfect - note added!")
        return redirect(url_for("notes", language=language))
    elif request.method == "GET":
        pass 
    else:
        flash("Oops - check fields!", "error")
    return render_template("addnote.html", form=form, language=language, sample1=sample1, sample2=sample2, sample3=sample3, sample4=sample4, quote=quote)


#EDIT_NOTE - allows a user owner edit a note if they own that note.
@app.route("/editnote/<language>/<noteid>", methods=["GET", "POST"])
@login_required
def editnote(language, noteid):
    form = NoteForm()
    note = mongo.db.notes.find_one_or_404({"_id": ObjectId(noteid),"user_id": ObjectId(current_user.id)})
    document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
    topics = document_language["topics"]
    form.topic.choices = [("", "-select-")]+[(topic, topic) for topic in topics]
    if form.validate_on_submit():
        mongo.db.notes.update_one({"_id": ObjectId(noteid)},{"$set": {"topic": form.topic.data, "note_name": form.name.data ,"content": form.content.data}})
        flash("Perfect - note updated!")
        return redirect(url_for("notes", language=language))
    elif request.method == "GET":
        form.topic.data = note["topic"]
        form.name.data = note["note_name"]
        form.content.data = note["content"]
    else:
        flash("Oops - check fields!", "error")   
    return render_template("editnote.html", form=form, note=note, language=language, sample1=sample1, sample2=sample2, sample3=sample3, sample4=sample4, quote=quote)
#WHY: user_id added as notes filter to ensure only the owner can edit a note.


#DELETE_NOTE - allows a user delete a note if they own that note.
@app.route("/deletenote/<language>/<noteid>", methods=["POST"]) #just post???
@login_required
def deletenote(language, noteid):
    mongo.db.notes.find_one_or_404({"_id": ObjectId(noteid), "user_id": ObjectId(current_user.id)})
    mongo.db.notes.delete_one({"_id": ObjectId(noteid)})
    flash("Perfect - note deleted!") 
    return redirect(url_for("notes", language=language))
#WHY: user_id added as notes filter to ensure only the owner can delete a note.


#FLAG LINK - allows a user report a problem with a link
@app.route("/flaglink/<language>/<linkid>", methods=["POST"])
def flaglink(language, linkid):
    mongo.db.links.find_one_or_404({"_id": ObjectId(linkid)})
    mongo.db.links.update_one({"_id": ObjectId(linkid)},{"$set": {"flag": True}})
    flash("Perfect - problem reported!")
    sleep(1)
    return redirect(url_for("links", language=language))
#WHERE: Sleep function from https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
#WHY: Sleep function used to allow user see icon color change before redirect.    


#RATE LINK - allows a user assign a 5 star rating to a link
@app.route("/ratelink/<language>/<linkid>/<rating>", methods=["POST"])
def ratelink(language, linkid, rating):
    mongo.db.links.find_one_or_404({"_id": ObjectId(linkid)})
    mongo.db.links.update_one({"_id": ObjectId(linkid)},{"$push": {"ratings": int(rating)}})
    flash("Perfect - link rated!")
    sleep(1)
    return redirect(url_for("links", language=language))  
#WHERE: Sleep function from https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
#WHY: Sleep function used to allow user see icon color change before redirect. 


#LOGOUT
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Perfect - logged out!") 
    return redirect(url_for("index"))   
#WHERE: Logout function from Flask Login documentation https://flask-login.readthedocs.io/en/latest/      


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)