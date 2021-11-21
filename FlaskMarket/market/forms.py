from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField

class Registration(FlaskForm):
    username = StringField(label="User Name")
    email_address = StringField(label="Email Address")
    password1 = PasswordField(label="Password")
    password2 = PasswordField(label="Conform Password")
    submit = SubmitField(label="Create Account")





