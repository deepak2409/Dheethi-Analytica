# app/SurveyForms/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Department, Role


class AppraisalForm(FlaskForm):
    """
    Form for taking appraisal input 
    """
    name = StringField('Name', validators=[DataRequired()])
    test1 = RadioField('Q1', choices = [('1','Good'),('2','Not Good')])
    # description = RadioField('Description', choices = [('CA','California'),('NV','Nevada')])
    test2 = RadioField('Q2', choices = [('1','Good'),('2','Not Good')])
    submit = SubmitField('Submit')