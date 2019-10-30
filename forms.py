from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, RadioField
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

class AddNoteForm(FlaskForm):
    language = SelectField('Language', validators=[DataRequired()], choices=[('html', 'HTML'), ('css', 'CSS'), ('js', 'JavaScript'), ('python', 'Python')])
    topic = SelectField('Topic', validators=[DataRequired()], choices=[('topic1', 'Topic1'), ('topic2', 'Topic2'), ('topic3', 'Topic3')])
    name = StringField('Note Name', validators=[DataRequired()])   
    point_type = SelectField('Point Type', validators=[DataRequired()], choices=[('description', 'Description'), ('syntax', 'Syntax'), ('know', 'Know'), ('code', 'Code')])
    point_content= StringField('Point Content', validators=[DataRequired()])
    submit = SubmitField('Save')

class AddLinkForm(FlaskForm):
    language = RadioField('Language', validators=[InputRequired()], choices=[('html', 'HTML'), ('css', 'CSS'), ('js', 'JavaScript'), ('python', 'Python')]) 
    topic = SelectField('Topic', validators=[InputRequired()], choices=[('', '--select--'), ('topic1', 'Topic1'), ('topic2', 'Topic2'), ('topic3', 'Topic3')])
    url = StringField('URL', validators=[InputRequired(), URL()]) 
    name = StringField('Name', validators=[InputRequired()])    
    link_type = RadioField('Type', validators=[InputRequired()], choices=[('instruct', 'Instruct'), ('practice', 'Practice'), ('resource', 'Resource'), ('other', 'Other')])
    rate = RadioField('Rate', validators=[InputRequired()], choices=[('1', '*'), ('2', '**'), ('3', '***'),('4', '****'), ('5', '*****')])
    description = TextAreaField('Description')
    submit = SubmitField('Save')    

