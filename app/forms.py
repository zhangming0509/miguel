# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, length


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired(), length(max=10)])
    remember_me = BooleanField('remember_me', default=False)
