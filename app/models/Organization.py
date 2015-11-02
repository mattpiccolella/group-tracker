from app import db
from datetime import datetime
from flask.ext.mongoengine.wtf import model_form

class Organization(db.Document):
    date_created = db.DateTimeField(required=True, default=datetime.now())
    date_modified = db.DateTimeField(required=True, default=datetime.now())
    name = db.StringField(required=True, max_length=510)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, max_length=510)

    # MongoEngine ORM metadata
    meta = {
        'allow_inheritance': True,
        'indexes': ['email', ]
    }
    def clean(self):
        self.date_modified = datetime.now()

    def __repr__(self):
        return '<User name={}, email={}>'.format(self.name, self.email)
