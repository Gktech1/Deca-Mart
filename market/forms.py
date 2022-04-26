from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    first_name = StringField(label='First Name')
    last_name = StringField(label='Last Name')
    email_address = StringField(label='Email')
    role = StringField(label='Role')
    password = StringField(label='password')
    confirm_password = StringField(label='confirm_password')