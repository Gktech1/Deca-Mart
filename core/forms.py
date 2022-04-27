from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError, Email
from core.models import Users

class RegisterForm(FlaskForm):

    def validate_email(self, email_to_check):
        email = Users.query.filter_by(email = email_to_check.data).first()
        if email:
            raise ValidationError("Email address already exists")
        
    first_name = StringField(label = 'first_name', validators= [DataRequired()])
    last_name = StringField(label = 'last_name', validators= [DataRequired()])
    email = StringField(label = 'email', validators= [Email(),DataRequired()])
    role = SelectField(label = 'register as', choices=[('Merchant', 'Merchant'), ('Buyer', 'Buyer1')])
    password = PasswordField(label='password', validators= [Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='confirm password', validators= [EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    email = StringField(label = 'email', validators= [DataRequired()])
    password = PasswordField(label='password', validators= [DataRequired()])
    submit = SubmitField(label='Login')