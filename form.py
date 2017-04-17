#credit to: http://burhan.io/flask-web-api-with-firebase/

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

Class FirePut(Form):
    title = StringField(‘title’, validators=[DataRequired()])
    field = StringField(‘field’, validators=[DataRequired()])
    url = StringField(‘url’, validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    description = StringField('description', validators = [DataRequired()])
