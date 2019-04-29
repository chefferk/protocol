from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from protocol.models import User


class RegistrationForm(FlaskForm):
    first_name = StringField('First', validators=[DataRequired()])
    last_name = StringField('Last', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Take the survey')


class BackgroundForm(FlaskForm):
    background = TextAreaField('Background', validators=[DataRequired()])
    submit = SubmitField('Proceed')


class CommentsForm(FlaskForm):
    comments = TextAreaField('Comments')
    submit = SubmitField('Finish')


class Task2Form(FlaskForm):
    rational = TextAreaField('Rational', validators=[DataRequired()])
    submit = SubmitField('Proceed')


class Task3Form(FlaskForm):
    rationals = TextAreaField('Rationals', validators=[DataRequired()])
    positions = TextAreaField('positions', validators=[DataRequired()])
    submit = SubmitField('Proceed')
