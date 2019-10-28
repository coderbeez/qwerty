from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class AddNoteForm(FlaskForm):
    category = SelectField('Category', validators=[DataRequired()], choices=[('cat1', 'Category 1'), ('cat2', 'Category2'), ('cat3', 'Category3')])
    name = StringField('Note Name', validators=[DataRequired()])   
    point_type = SelectField('Point Type', validators=[DataRequired()], choices=[('description', 'Description'), ('syntax', 'Syntax'), ('know', 'Know'), ('code', 'Code')])
    point_content= StringField('Point Content', validators=[DataRequired()])
    submit = SubmitField('Save')

class AddLinkForm(FlaskForm):
    category = SelectField('Category', validators=[DataRequired()], choices=[('cat1', 'Category 1'), ('cat2', 'Category2'), ('cat3', 'Category3')])
    url = StringField('URL', validators=[DataRequired()]) 
    name = StringField('Name', validators=[DataRequired()])    
    link_type = RadioField('Type', validators=[DataRequired()], choices=[('instruct', 'Instruct'), ('practice', 'Practice'), ('resource', 'Resource'), ('other', 'Other')])
    rate = StringField('Rate', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Save')    

