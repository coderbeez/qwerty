from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, RadioField, FieldList, FormField
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

#class PointForm(FlaskForm):
    #ppoint_type = SelectField('Point Type', validators=[InputRequired()], choices=[('', '--select--'),('Description', 'Description'), ('Syntax', 'Syntax'), ('Know', 'Know'), ('Code', 'Code')])
    #ppoint_content= TextAreaField('Point Content', validators=[InputRequired()])
    #psubmit = SubmitField('Save')   

class NoteForm(FlaskForm):
    language = RadioField('Language', validators=[DataRequired()], choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript', 'JavaScript'), ('Python', 'Python')]) 
    topic = SelectField('Topic', validators=[DataRequired()], choices=[('', '--select--'),('Fundamentals', 'Fundamentals'), ('Topic2', 'Topic2'), ('Topic3', 'Topic3')])
    name = StringField('Title', validators=[DataRequired()])
    content= TextAreaField('Content', validators=[DataRequired()])   
    #points = FieldList(FormField(PointForm), min_entries=0)
    #point_type = SelectField('Point Type', validators=[], choices=[('', '--select--'),('Description', 'Description'), ('Syntax', 'Syntax'), ('Know', 'Know'), ('Code', 'Code')])
    #point_content= TextAreaField('Point Content', validators=[])
    submit = SubmitField('Save')

class LinkForm(FlaskForm):
    language = RadioField('Language', validators=[InputRequired()], choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript', 'JavaScript'), ('Python', 'Python')]) 
    topic = SelectField('Topic', validators=[InputRequired()], choices=[('', '--select--'), ('Fundamentals', 'Fundamentals'), ('Topic2', 'Topic2'), ('Topic3', 'Topic3')])
    url = StringField('URL', validators=[InputRequired(), URL()]) 
    name = StringField('Name', validators=[InputRequired()])    
    link_type = RadioField('Type', validators=[InputRequired()], choices=[('Instruct', 'Instruct'), ('Practice', 'Practice'), ('Resource', 'Resource'), ('Other', 'Other')])
    rate = RadioField('Rate', validators=[InputRequired()], choices=[('1', '*'), ('2', '**'), ('3', '***'),('4', '****'), ('5', '*****')])
    description = TextAreaField('Description')
    submit = SubmitField('Save')    

