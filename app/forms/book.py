__author__ = "to2bage"

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=32, message="必须填写"), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message="1<<x<<99")], default=1)