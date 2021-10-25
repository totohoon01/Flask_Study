# WTForms 기반 폼 데이터 처리
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    subject = StringField("제목", validators=[DataRequired()])
    content = TextAreaField("제목", validators=[DataRequired()])
