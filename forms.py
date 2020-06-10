from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class signupform(FlaskForm):
    iname = StringField('Individual Name', validators=[DataRequired(), Length(min=2, max=20)])
    dob = DateField('Date of Birth', validators=[DataRequired()], format = '%d/%m/%Y')
    address = StringField('Address', validators=[DataRequired(), Length(min=5, max=50)])
    uname = StringField('Users name', validators=[DataRequired(), Length(min=2, max=20)])
    relation = SelectField('Relation with the Individual', choices=[('son', 'Son'), ('da', 'Daughter'), ('ct', 'CareTaker'), ('gu', 'Guardian')])
    contact = StringField('Emergency Contact Number', validators=[DataRequired(), Length(min=10, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    signup = SubmitField('Sign up')

class signinform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    signin = SubmitField('Sign in')

class Dashboard(FlaskForm):
    viewcamera = SubmitField('View Surviellance')
    update = SubmitField('Update Profile')
    logout = SubmitField('Logout')