# app/SurveyForms/views.py

from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user

from . import SurveyForms

from . import forms
from .forms import AppraisalForm
from .. import db
from ..models import Employee, empEng


# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     """
#     Handle requests to the /register route
#     Add an employee to the database through the registration form
#     """
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         employee = Employee(email=form.email.data,
#                             username=form.username.data,
#                             first_name=form.first_name.data,
#                             last_name=form.last_name.data,
#                             password=form.password.data)

#         # add employee to the database
#         db.session.add(employee)
#         db.session.commit()
#         flash('You have successfully registered! You may now login.')

#         # redirect to the login page
#         return redirect(url_for('auth.login'))

#     # load registration template
#     return render_template('auth/register.html', form=form, title='Register')


# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     """
#     Handle requests to the /login route
#     Log an employee in through the login form
#     """
#     form = LoginForm()
#     if form.validate_on_submit():

#         # check whether employee exists in the database and whether
#         # the password entered matches the password in the database
#         employee = Employee.query.filter_by(email=form.email.data).first()
#         if employee is not None and employee.verify_password(
#                 form.password.data):
#             # log employee in
#             login_user(employee)

#              # redirect to the appropriate dashboard page
#             if employee.is_admin:
#                 return redirect(url_for('home.admin_dashboard'))
#             else:
#                 return redirect(url_for('home.dashboard'))

           

#         # when login details are incorrect
#         else:
#             flash('Invalid email or password.')

#     # load login template
#     return render_template('auth/login.html', form=form, title='Login')


# @auth.route('/logout')
# @login_required
# def logout():
#     """
#     Handle requests to the /logout route
#     Log an employee out through the logout link
#     """
#     logout_user()
#     flash('You have successfully been logged out.')

#     # redirect to the login page
#     return redirect(url_for('auth.login'))

@SurveyForms.route('/Appraisal', methods=['GET', 'POST'] )
@login_required
def Appraisal():
    """
    Render the Appraisal template on the /Appraisal route
    """
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    # form = AppraisalForm()
    # if form.validate_on_submit():
    #     return 'Success'
    # return render_template('SurveyForms/trial.html', title = 'Appraisal')
    if request.method == "GET":
        
        return render_template('SurveyForms/trial.html', title = 'Appraisal')
    if request.method == "POST":
        

        q14_howMany =      request.form["q14_howMany"]
        q13_pleaseRate_0 = request.form["q13_pleaseRate[0]"]
        q13_pleaseRate_1 = request.form["q13_pleaseRate[1]"]
        q13_pleaseRate_2 = request.form["q13_pleaseRate[2]"]
        q13_pleaseRate_3 = request.form["q13_pleaseRate[3]"]
        q13_pleaseRate_4 = request.form["q13_pleaseRate[4]"]
        q13_pleaseRate_5 = request.form["q13_pleaseRate[5]"]
        q13_pleaseRate_6 = request.form["q13_pleaseRate[6]"]
        q3_howWould3_0   = request.form["q3_howWould3[0]"]
        q3_howWould3_1   = request.form["q3_howWould3[1]"]
        q3_howWould3_2   = request.form["q3_howWould3[2]"]
        q3_howWould3_3   = request.form["q3_howWould3[3]"]
        q3_howWould3_4   = request.form["q3_howWould3[4]"]
        q4_typeA4_0      = request.form["q4_typeA4[0]"]
        q4_typeA4_1      = request.form["q4_typeA4[1]"]
        q4_typeA4_2      =request.form["q4_typeA4[2]"]
        q4_typeA4_3      = request.form["q4_typeA4[3]"]
        q5_howWould_0    = request.form["q5_howWould[0]"]
        q5_howWould_1    = request.form["q5_howWould[1]"]
        q5_howWould_2    = request.form["q5_howWould[2]"]
        q5_howWould_3    = request.form["q5_howWould[3]"]
        q5_howWould_4    = request.form["q5_howWould[4]"]
        q6_howWould6_0   = request.form["q6_howWould6[0]"]
        q6_howWould6_1   = request.form["q6_howWould6[1]"]
        q6_howWould6_2   = request.form["q6_howWould6[2]"]
        q6_howWould6_3   = request.form["q6_howWould6[3]"]
        q6_howWould6_4   = request.form["q6_howWould6[4]"]
        q10_anyComments10 = request.form["q10_anyComments10"]
        q7_name_first    = request.form["q7_name[first]"]
        q7_name_last     = request.form["q7_name[last]"]
        q8_email         = request.form["q8_email"]
        rec = empEng(q14_howMany = q14_howMany ,q13_pleaseRate_0= q13_pleaseRate_0  ,q13_pleaseRate_1 = q13_pleaseRate_1,q13_pleaseRate_2 = q13_pleaseRate_2 ,q13_pleaseRate_3 = q13_pleaseRate_3  ,q13_pleaseRate_4 = q13_pleaseRate_4,q13_pleaseRate_5 = q13_pleaseRate_5  ,q13_pleaseRate_6 = q13_pleaseRate_6,q3_howWould3_0 = q3_howWould3_0,q3_howWould3_1 = q3_howWould3_1  ,q3_howWould3_2 = q3_howWould3_2, q3_howWould3_3 = q3_howWould3_3  ,q3_howWould3_4 = q3_howWould3_4,q4_typeA4_0 = q4_typeA4_0,q4_typeA4_1 = q4_typeA4_1  ,q4_typeA4_2 = q4_typeA4_2,q4_typeA4_3= q4_typeA4_3  ,q5_howWould_0 = q5_howWould_0,q5_howWould_1 = q5_howWould_1,q5_howWould_2= q5_howWould_2  ,q5_howWould_3 = q5_howWould_3  ,q5_howWould_4 = q5_howWould_4,q6_howWould6_0 = q6_howWould6_0  ,q6_howWould6_1  = q6_howWould6_1,q6_howWould6_2= q6_howWould6_2  ,q6_howWould6_3 = q6_howWould6_3  ,q6_howWould6_4 = q6_howWould6_4,q10_anyComments10 = q10_anyComments10,q7_name_first = q7_name_first,q7_name_last = q7_name_last,q8_email  = q8_email)
        # add rec to the database
        db.session.add(rec)
        db.session.commit()
        print(len(q13_pleaseRate_0))
        flash('You have successfully provided the surevey inputs!')
        # redirect to the login page
        return 'Success'
      
      
       # @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     """
#     Handle requests to the /register route
#     Add an employee to the database through the registration form
#     """
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         employee = Employee(email=form.email.data,
#                             username=form.username.data,
#                             first_name=form.first_name.data,
#                             last_name=form.last_name.data,
#                             password=form.password.data)

#         # add employee to the database
#         db.session.add(employee)
#         db.session.commit()
#         flash('You have successfully registered! You may now login.')

#         # redirect to the login page
#         return redirect(url_for('auth.login'))

#     # load registration template
#     return render_template('auth/register.html', form=form, title='Register')


       