from flask import Flask


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Home Page"


@app.route("/login")
def login():
    return "Login Page"


@app.route("/register")
def register():
    return "Register Page"


@app.route("/notes")
def notes():
    return "Notes Page"


@app.route("/addnote")
def addnote():
    return "Add Note Page"


@app.route("/editnote")
def editnote():
    return "Edit Note Page"


@app.route("/links")
def links():
    return "Links Page"


@app.route("/addlink")
def addlink():
    return "Add Link Page"   


if __name__ == '__main__':
    app.run(debug=True)