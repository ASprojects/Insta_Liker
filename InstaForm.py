from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Numer telefonu, nazwa lub e-mail:", validators=[DataRequired()])
    password = PasswordField("Haslo:", validators=[DataRequired()])
    hashtag = StringField("Hasztag:", validators=[DataRequired()])
    remember = BooleanField("Zapamietaj mnie")
    submit = SubmitField("Do dziela!")

