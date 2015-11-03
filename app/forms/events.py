from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required

EMAIL_ERROR = 'Please provide a valid email address for this organization.'

class CreateEventForm(Form):
    name = StringField('Full Name', [Required("Please type a name for your event")])

class EventCheckinForm(Form):
    name = StringField('Enter your name', [Required("Please enter your name")])
