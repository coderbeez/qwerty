from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, RadioField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, URL

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Login')


class NoteForm(FlaskForm):
    topic = SelectField('Topic', validators=[InputRequired()])
    name = StringField('Title', validators=[InputRequired()])
    content= TextAreaField('Content', validators=[InputRequired()])   
    submit = SubmitField('Save')

class LinkForm(FlaskForm):
    topic = SelectField('Topic', validators=[InputRequired()]) #Input or Data Required?
    url = StringField('URL', validators=[InputRequired(), URL()]) 
    name = StringField('Name', validators=[InputRequired()])    
    link_type = RadioField('Type', validators=[InputRequired()], choices=[('instruct', 'instruct'), ('practice', 'practice'), ('resource', 'resource'), ('other', 'other')])
    rate = IntegerField('Rate', validators=[])
    description = TextAreaField('Description')
    submit = SubmitField('Save')    

class SearchForm(FlaskForm):
    tsearch = StringField('Text', validators=[InputRequired()])
    submit = SubmitField('Search') 
