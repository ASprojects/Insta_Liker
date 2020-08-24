from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Numer telefonu, nazwa konta lub e-mail:", validators=[DataRequired()])
    password = PasswordField("Haslo:", validators=[DataRequired()])
    hashtag = StringField("Hasztag:", validators=[DataRequired()])
    remember = BooleanField("Nie zaznaczaj tego")
    submit = SubmitField("Do dziela!")