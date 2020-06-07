from flask import Blueprint

SurveyForms = Blueprint('SurveyForms', __name__)

from . import views