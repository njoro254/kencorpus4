from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, SelectField
from wtforms.fields import EmailField, DateField
from wtforms.validators import ValidationError
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField
from prints.auth.models import FieldToolUser_Table


import re




class ChiefRegistrationForm(Form):
    first_name = StringField(' First Name', [
        validators.DataRequired()])

    last_name = StringField('Last Name', [
        validators.DataRequired()])

    email = EmailField('Email address', [
        validators.DataRequired(), 
        validators.Email()])

    username = StringField('Username', [
        validators.DataRequired(), 
        validators.Length(min=4, max=25)])



    password = PasswordField('Password', [
        validators.DataRequired(), 
        validators.EqualTo('confirm', message='Passwords must match'), 
        validators.length(min=4, max=80)])

    confirm = PasswordField('Repeat Password')




class StaffRegistrationForm(Form):
    first_name = StringField(' First Name', [
        validators.DataRequired()])

    last_name = StringField('Last Name', [
        validators.DataRequired()])

    email = EmailField('Email address', [
        validators.DataRequired(), 
        validators.Email()])

    username = StringField('Username', [
        validators.DataRequired(), 
        validators.Length(min=8, max=25)])

    specialty=SelectField('Specialty', [
        validators.DataRequired()], choices=[("Investigator","Investigator"),
        ("Research Assisstant","Research Assisstant"),
        ("Proof of Concept","Proof of Concept")] )

    specialty_description=StringField('Describe the Specialty', 
        [validators.DataRequired()])



    password = PasswordField('Password', [
        validators.DataRequired(), 
        validators.EqualTo('confirm', message='Passwords must match'), 
        validators.length(min=10, max=80)])

    confirm = PasswordField('Repeat Password')






class LoginForm(Form):
    username = StringField('Username', [
            validators.DataRequired(),
            validators.Length(min=8, max=25)
        ])

    password = PasswordField('Password', [
            validators.DataRequired(),
            validators.Length(min=8, max=80)
        ])



class ForgotPasswordForm(Form):
    email = StringField(' Email ', [
        validators.DataRequired()])

  























#########################################################################################
#Test forms
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

unverified_list=[]
for name in FieldToolUser_Table.objects.all().values_list():
    if name.verification_status=="False":
        unverified_list.append(name.username)


class UnVerifiedForm(FlaskForm):
    # create a list of value/description tuples
    unveriftuple = [(x, x) for x in unverified_list]
    unverifiedusernames = MultiCheckboxField('Label', choices=unveriftuple)
