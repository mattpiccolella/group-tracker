from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Required, Email, EqualTo

EMAIL_ERROR = 'Please provide a valid email address for this organization.'

class CreateOrganizationForm(Form):
    name = StringField('Full Name', [Required("Please type a name for your organization")])
    email = StringField('Email Address',
                        [Email(message=EMAIL_ERROR),
                         Required(message=EMAIL_ERROR)])
    password = PasswordField('New Password', [
        Required("Please provide a password for your organization."),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')



