from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("Please Enter First Name.")])
	middle_name = StringField('Middle Name')
	last_name = StringField('Last Name', validators=[DataRequired("Please Enter Last Name.")])
	email = StringField('Email', 
		                 validators=[DataRequired("Please Enter Email."), 
		                 Email("Please Enter Valid Email Address.")])
	password = PasswordField('Password', validators=[DataRequired("Password Field Can't be empty."), Length(min=6, message="Password must be 6 or more characters")])
	submit = SubmitField('Sign Up')

class LoginForm(Form):
	email = StringField('Email', 
		                 validators=[DataRequired("Please Enter Email"), 
		                 Email("Please Enter Valid Email Address")])
	password = Password('Password', validators=[DataRequired("Please Enter Password.")])
	submit = SubmitField('Sign in')