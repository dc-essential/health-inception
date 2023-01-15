from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterUserForm(FlaskForm):
    name = StringField("User name", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Provide valid email")])
    password = PasswordField(label='Password', validators=[DataRequired(message='Field must be at least 8 characters long'), Length(min=8)])
    submit = SubmitField(label="Register")

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Provide valid email")])
    password = PasswordField(label='Password', validators=[DataRequired(message='Field must be at least 8 characters long'), Length(min=8)])
    submit = SubmitField(label="Login")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")