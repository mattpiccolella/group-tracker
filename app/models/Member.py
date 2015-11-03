from app import db
from app.models.Organization import Organization
from datetime import datetime

class Member(db.Document):
    name = db.StringField(required=True, max_length=500)
    organization = db.ReferenceField(Organization)

    # MongoEngine ORM metadata
    meta = {
        'allow_inheritance': True,
        'indexes': ['organization', ]
    }

    def __repr__(self):
        return '<Member name={}>'.format(self.name)
