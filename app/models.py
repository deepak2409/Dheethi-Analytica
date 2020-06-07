# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class empEng(db.Model):

    __tablename__ = "empEngs"

    id = db.Column(db.Integer, primary_key=True)
    q14_howMany = db.Column(db.String(50))
    q13_pleaseRate_0 = db.Column(db.String(50))
    q13_pleaseRate_1 = db.Column(db.String(50))
    q13_pleaseRate_2 = db.Column(db.String(50))
    q13_pleaseRate_3 = db.Column(db.String(50))
    q13_pleaseRate_4 = db.Column(db.String(50))
    q13_pleaseRate_5 = db.Column(db.String(50))
    q13_pleaseRate_6 = db.Column(db.String(50))
    q3_howWould3_0   = db.Column(db.String(50))
    q3_howWould3_1   = db.Column(db.String(50))
    q3_howWould3_2   = db.Column(db.String(50))
    q3_howWould3_3   = db.Column(db.String(50))
    q3_howWould3_4   = db.Column(db.String(50))
    q4_typeA4_0      = db.Column(db.String(50))
    q4_typeA4_1      = db.Column(db.String(50))
    q4_typeA4_2      = db.Column(db.String(50))
    q4_typeA4_3      = db.Column(db.String(50))
    q5_howWould_0    = db.Column(db.String(50))
    q5_howWould_1    = db.Column(db.String(50))
    q5_howWould_2    = db.Column(db.String(50))
    q5_howWould_3    = db.Column(db.String(50))
    q5_howWould_4    = db.Column(db.String(50))
    q6_howWould6_0   = db.Column(db.String(50))
    q6_howWould6_1   = db.Column(db.String(50))
    q6_howWould6_2   = db.Column(db.String(50))
    q6_howWould6_3   = db.Column(db.String(50))
    q6_howWould6_4   = db.Column(db.String(50))
    q10_anyComments10 = db.Column(db.String(4096))
    q7_name_first    = db.Column(db.String(25))
    q7_name_last     = db.Column(db.String(25))
    q8_email         = db.Column(db.String(25))


